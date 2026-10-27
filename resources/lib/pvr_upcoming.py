# -*- coding: utf-8 -*-
import json
import sys
from datetime import datetime, timezone
from urllib.parse import parse_qsl, unquote

import xbmc
import xbmcgui
import xbmcplugin


def _jsonrpc(method, params=None):
    payload = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params is not None:
        payload["params"] = params
    try:
        raw = xbmc.executeJSONRPC(json.dumps(payload))
        return json.loads(raw).get("result") or {}
    except Exception:
        return {}


def _parse_utc(dt_str):
    if not dt_str:
        return None
    try:
        return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _to_local_hhmm(dt_str):
    dt = _parse_utc(dt_str)
    if not dt:
        return ""
    return dt.astimezone().strftime("%H:%M")


def _find_channel_id(channel_path, channel_number, channel_name, is_radio=False):
    group = "allradio" if is_radio else "alltv"
    res = _jsonrpc(
        "PVR.GetChannels",
        {
            "channelgroupid": group,
            "properties": ["uniqueid", "channelnumber", "subchannelnumber", "channel"],
        },
    )
    channels = res.get("channels") or []
    if not channels:
        return None

    # 1. Match by uniqueid extracted from pvr://.../addon_12345.pvr
    if channel_path and ".pvr" in channel_path and "_" in channel_path:
        try:
            uid_part = channel_path.rsplit("_", 1)[-1].split(".pvr", 1)[0]
            uid = int(uid_part)
            for ch in channels:
                if ch.get("uniqueid") == uid:
                    if not channel_name or ch.get("label") == channel_name or ch.get("channel") == channel_name:
                        return ch.get("channelid")
            for ch in channels:
                if ch.get("uniqueid") == uid:
                    return ch.get("channelid")
        except ValueError:
            pass

    # 2. Match by channel number + name
    if channel_number:
        for ch in channels:
            num = str(ch.get("channelnumber", ""))
            sub = ch.get("subchannelnumber", 0)
            formatted_num = f"{num}.{sub}" if sub else num
            if formatted_num == channel_number:
                if not channel_name or ch.get("label") == channel_name or ch.get("channel") == channel_name:
                    return ch.get("channelid")

    # 3. Match by channel name
    if channel_name:
        for ch in channels:
            if ch.get("label") == channel_name or ch.get("channel") == channel_name:
                return ch.get("channelid")

    # 4. Fallback to channel number only
    if channel_number:
        for ch in channels:
            num = str(ch.get("channelnumber", ""))
            if num == channel_number:
                return ch.get("channelid")

    return None


def main():
    handle = int(sys.argv[1]) if len(sys.argv) > 1 else -1
    if handle < 0:
        return

    query = sys.argv[2][1:] if len(sys.argv) > 2 and sys.argv[2].startswith("?") else ""
    params = dict(parse_qsl(query))

    channel_path = unquote(params.get("path", "")).strip()
    channel_number = unquote(params.get("channelnumber", "")).strip()
    channel_name = unquote(params.get("channelname", "")).strip()
    try:
        limit = int(params.get("limit", "5"))
    except ValueError:
        limit = 5

    # Only resolve for PVR channel items
    if not channel_path and not channel_number and not channel_name:
        xbmcplugin.endOfDirectory(handle, succeeded=True, cacheToDisc=False)
        return
    if channel_path and not channel_path.startswith("pvr://channels/"):
        xbmcplugin.endOfDirectory(handle, succeeded=True, cacheToDisc=False)
        return

    is_radio = "pvr://channels/radio/" in channel_path
    channel_id = _find_channel_id(channel_path, channel_number, channel_name, is_radio=is_radio)
    if not channel_id:
        xbmcplugin.endOfDirectory(handle, succeeded=True, cacheToDisc=False)
        return

    res = _jsonrpc(
        "PVR.GetBroadcasts",
        {
            "channelid": channel_id,
            "properties": [
                "title",
                "starttime",
                "endtime",
                "runtime",
                "genre",
                "plot",
                "plotoutline",
                "episodename",
                "episodenum",
                "seasonnum",
                "isactive",
            ],
        },
    )
    broadcasts = res.get("broadcasts") or []
    now_utc = datetime.now(timezone.utc)

    upcoming = []
    for bc in broadcasts:
        if bc.get("isactive"):
            continue
        start_dt = _parse_utc(bc.get("starttime", ""))
        if not start_dt or start_dt <= now_utc:
            continue
        upcoming.append((start_dt, bc))
        if len(upcoming) >= limit:
            break

    items = []
    for _, bc in upcoming:
        title = bc.get("title") or bc.get("label") or ""
        start_hhmm = _to_local_hhmm(bc.get("starttime", ""))
        end_hhmm = _to_local_hhmm(bc.get("endtime", ""))
        episode_name = (bc.get("episodename") or "").strip()
        season_num = bc.get("seasonnum")
        episode_num = bc.get("episodenum")

        # Resolve genre
        genre_raw = bc.get("genre") or []
        if isinstance(genre_raw, list):
            genre_str = ", ".join(g for g in genre_raw if g)
        else:
            genre_str = str(genre_raw) if genre_raw else ""

        # Check if season/episode is genuine (ignore dummy S1E1 on movies/broadcasts)
        is_series = False
        if episode_name:
            is_series = True
        elif season_num and episode_num:
            try:
                s_int = int(season_num)
                e_int = int(episode_num)
                if s_int > 1 or e_int > 1:
                    is_series = True
            except (ValueError, TypeError):
                pass
        elif episode_num:
            try:
                if int(episode_num) > 1:
                    is_series = True
            except (ValueError, TypeError):
                pass

        genre_lower = genre_str.lower()
        if any(kw in genre_lower for kw in ["spielfilm", "movie", "film", "nachrichten", "news", "sport"]):
            is_series = False

        # Format Season / Episode (e.g. S01E05)
        se_tag = ""
        if is_series:
            try:
                s_int = int(season_num) if season_num else 0
                e_int = int(episode_num) if episode_num else 0
                if s_int > 0 and e_int > 0:
                    se_tag = f"S{s_int:02d}E{e_int:02d}"
                elif e_int > 0:
                    se_tag = f"E{e_int:02d}"
                elif s_int > 0:
                    se_tag = f"S{s_int:02d}"
            except (ValueError, TypeError):
                pass

        # SubLine composition: Prioritize Episode Name, Season/Episode, and fallback to Genre/End time
        sub_parts = []
        if se_tag:
            sub_parts.append(se_tag)
        if episode_name:
            sub_parts.append(episode_name)

        if not sub_parts:
            # Fallback if no episode metadata is provided by EPG
            if genre_str:
                sub_parts.append(genre_str)
            if end_hhmm:
                sub_parts.append(f"Bis {end_hhmm}")

        subline_str = " · ".join(sub_parts)

        li = xbmcgui.ListItem(label=title, label2=start_hhmm, offscreen=True)
        li.setProperty("StartTime", start_hhmm)
        li.setProperty("EndTime", end_hhmm)
        li.setProperty("EpisodeName", episode_name)
        li.setProperty("Season", str(season_num) if season_num is not None else "")
        li.setProperty("Episode", str(episode_num) if episode_num is not None else "")
        li.setProperty("SubLine", subline_str)

        info_tag = li.getVideoInfoTag()
        info_tag.setTitle(title)
        if episode_name:
            info_tag.setTitle(episode_name)
        if bc.get("plot"):
            info_tag.setPlot(bc["plot"])

        items.append(("", li, False))

    if items:
        xbmcplugin.addDirectoryItems(handle, items, len(items))
    xbmcplugin.endOfDirectory(handle, succeeded=True, cacheToDisc=False)


if __name__ == "__main__":
    main()
