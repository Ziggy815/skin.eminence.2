# Eminence 2 (Kodi 22 „Piers“ Edition)

A clean, minimalist, and modern skin for Kodi.

> **Note:** This repository is a maintained and modernized **fork** of the original **[skin.eminence.2](https://github.com/jurialmunkey/skin.eminence.2)** by **jurialmunkey**.  
> It has been extensively updated and refactored for full compatibility with **Kodi 22 (Piers)** (`xbmc.gui` 5.18.0) as well as Kodi 21 (Omega) and Kodi 20 (Nexus).

---

## Key Features & Compatibility Updates

* **Full Kodi 22 „Piers“ Compatibility:**
  * Updated skin version and GUI dependency targeting `xbmc.gui` version `5.18.0`.
  * Fully resolved deprecated and removed InfoBools and functions (e.g. replaced `Player.DisplayAfterSeek` with `Player.HasPerformedSeek(3)`, modernized `Integer.IsGreater`, corrected `ListItem.DBType` syntax).
* **New Dialogs & Windows:**
  * **Video Manager (`DialogVideoManager.xml`):** Full native skin support for managing video versions and extras introduced in Kodi 21+.
  * **Native Color Picker (`DialogColorPicker.xml` & `colorbutton`):** Modernized settings color picker controls for subtitles and interface customization.
  * **Game & RetroPlayer Integration:** Added support for In-Game Saves (`ingamesaves`), Game Controller Ports (`gameports`), Game OSD features, and Savestate previews.
  * **PVR Enhancements:** Added support for PVR Providers (`MyPVRProviders.xml`) and updated channel guide views.
  * **Video & Music Info Dialogs:** Added buttons for managing video versions, extras, user ratings, and album/artist playback.
* **Continuous Integration:** Automated XML syntax validation via GitHub Actions workflow (`tests/validate_xml.py`).

For an in-depth list of all technical fixes, adjustments, and changes, please refer to [**CHANGELOG_KODI22.md**](CHANGELOG_KODI22.md).

---

## Dependencies & Supported Addons

The skin automatically utilizes the following addons when installed:

* **Required:**
  * `script.skinshortcuts`
  * `script.image.resource.select`
  * `resource.images.weathericons.white`
* **Supported / Optional:**
  * `plugin.video.themoviedb.helper` (The Movie Database Helper)
  * `plugin.program.autocompletion`

---

## Credits & Attribution

* Original skin concept and creation by **[jurialmunkey](https://github.com/jurialmunkey)**.
* Additional translations, improvements, and Kodi 22 compatibility updates by contributors and maintainers.

---

## License

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License (CC BY-NC-SA 3.0)**.  
To view a copy of this license, visit [http://creativecommons.org/licenses/by-nc-sa/3.0/](http://creativecommons.org/licenses/by-nc-sa/3.0/) or refer to [LICENSE.txt](LICENSE.txt).