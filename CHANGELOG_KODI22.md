# Changelog – Anpassungen für Kodi 22 „Piers“ (`xbmc.gui` 5.18.0)

Dieser Changelog dokumentiert alle Prüfungen, Fehlerbehebungen und Erweiterungen am Skin `skin.eminence.2`, um 100 % Kompatibilität mit der aktuellen Kodi-Entwicklerversion (**Kodi 22 „Piers“**, `xbmc.gui` Version `5.18.0`, einschließlich aller Skinning-Engine-Änderungen aus Kodi 19 „Matrix“, Kodi 20 „Nexus“ und Kodi 21 „Omega“) sicherzustellen.

---

## 1. Entfernte & fehlerhafte InfoBools, Funktionen und Window-Aufrufe behoben

- **`Player.DisplayAfterSeek` → `Player.HasPerformedSeek(3)` (in Kodi 20 entfernt):**
  - `16x9/DialogSeekBar.xml` (Zeile 6)
  - `16x9/Includes_Window.xml` (alle 8 Vorkommen ersetzt sowie leeres `<visible></visible>` entfernt)
  - `16x9/MusicOSD.xml` (2 Vorkommen ersetzt)
  - `16x9/MusicVisualisation.xml` (Zeile 85)
- **Fehlerhafte InfoBool-Syntax `String.String.IsEmpty(Listitem.dbtype)` → `String.IsEmpty(ListItem.DBType)`:**
  - `16x9/Includes_Image.xml` (2 Vorkommen)
  - `16x9/Viewtype_List.xml` (9 Vorkommen)
- **Entfernte Legacy-Bedingung `IntegerGreaterThan(System.ProfileCount,1)` → `Integer.IsGreater(System.ProfileCount,1)`:**
  - `shortcuts/powermenu.DATA.xml`
  - `16x9/script-skinshortcuts-includes.xml`
- **Ungültiger Window-Name, Window-ID & XML-Syntaxfehler:**
  - `ActivateWindow(visualisationpreset)` → `ActivateWindow(visualisationpresetlist)` in `16x9/Includes_Window.xml`
  - Fehlerhafte `<window id="2">` (Kollision mit `MyPics.xml`) → `<window>` in `16x9/MyGames.xml`
  - Copy-Paste-Fehler `Container(53)` → `Container(535)` in `16x9/Viewtype_ShowCase.xml`
  - Doppelte schließende Klammer `</onclick>>` → `</onclick>` in `16x9/SkinSettings.xml`

---

## 2. Neue Dialoge & Controls für Kodi 20, 21 und 22 ergänzt

### Video Versions & Video Extras (Kodi 21+)
- **`16x9/DialogVideoManager.xml` (neu erstellt):**
  - Unterstützt sowohl `managevideoversions` als auch `managevideoextras` im Eminence-Design (Liste `id="50"`, Scrollbar `id="60"` sowie alle Steuerungsbuttons `id="21"` bis `id="29"`).
- **`16x9/DialogVideoInfo.xml` erweitert:**
  - Button `id="14"` (Video-Versionen verwalten / auswählen)
  - Button `id="15"` (Video-Extras)
  - Button `id="7"` (Eigene Bewertung / User Rating setzen)

### Music Info Dialog Play-Button (Kodi 20+)
- **`16x9/DialogMusicInfo.xml` erweitert:**
  - Play-Button `id="8"` zum direkten Abspielen von Alben und Künstlern ergänzt.

### Nativer Color-Picker & `colorbutton`-Control (Kodi 20+)
- **`16x9/Defaults.xml`:**
  - `<default type="colorbutton">` definiert.
- **`16x9/SettingsCategory.xml`, `16x9/DialogSettings.xml`, `16x9/DialogAddonSettings.xml`:**
  - `<control type="colorbutton" id="15">` ergänzt, damit Farbeinstellungen (z. B. für Untertitel) in den System- und Addon-Einstellungen sichtbar und bedienbar sind.
- **`16x9/DialogColorPicker.xml` (neu erstellt):**
  - Dialog zur Farbauswahl (`id="1"` Header, `id="6"` Farbpanel, `id="61"` Scrollbar, `id="7"` Abbrechen-Button).

### Spiele-Einstellungen, In-Game Saves & RetroPlayer-Dialoge (Kodi 19–22)
- **Spiele-Einstellungen im Haupt-Einstellungsmenü:**
  - `GameSettings`-Eintrag (`$LOCALIZE[15016]`) in `16x9/Includes_Defs.xml`, `16x9/Includes_Image.xml` und `16x9/Includes_Label.xml` ergänzt.
- **`16x9/GameOSD.xml`:**
  - Menüpunkte für Spielstände (`ActivateWindow(InGameSaves)`) und Controller-Ports (`ActivateWindow(GamePorts)`) ergänzt.
  - Sichtbarkeitsbedingungen um `GameVolume`, `GameAdvancedSettings`, `GamePorts`, `InGameSaves` und `GameAgents` erweitert.
- **`16x9/DialogSelect.xml` & `16x9/Includes_Dialog.xml` (`Dialog_Select_Game`):**
  - `Window.IsActive(ingamesaves)` in die Auswahlbedingung aufgenommen.
  - Container-ID auf `id="10811"` (vorher `11`) und Beschreibungs-Textbox auf `id="10812"` (vorher `12`) aktualisiert.
  - `<pixels>$INFO[ListItem.FilenameAndPath]</pixels>` in `<control type="gamewindow">` für die Savestate-Vorschau ergänzt.

---

## 3. PVR-, PlayerProcessInfo- & Favourites-Anpassungen (Kodi 20–22)

- **Fehlende PVR-Fenster und Dialoge neu erstellt:**
  - `16x9/MyPVRProviders.xml` für `tvproviders` / `radioproviders` (inklusive TopBar-Integration in `16x9/Includes_Furniture.xml`)
  - `16x9/DialogPVRGuideControls.xml` für die EPG-Grid-Navigation (`PVR.EpgGridControl(...)`)
  - `16x9/DialogPVRRadioRDSInfo.xml` für Radio-RDS-Informationen
- **`16x9/DialogPlayerProcessInfo.xml`:**
  - Anzeige für `VideoPlayer.HDRType` (HDR-Typ) und `PVR.TimeshiftProgressPlayPos` ergänzt.
- **Live-TV EPG-Endzeit, Laufzeit & Fortschrittsbalken (`Includes_Label.xml`, `Includes_Furniture.xml`, `Includes_Window.xml`):**
  - `Player.FinishTime`, `Player.Time`, `Player.Duration` und `Player.Progress` beziehen sich seit der PVR-Timeshift-Überarbeitung in Kodi auf den Timeshift-Puffer (wodurch `Player.FinishTime` bei Live-TV immer die aktuelle Systemzeit anzeigte).
  - Neue Variable `Label_FinishTime` in `16x9/Includes_Label.xml` eingeführt, die bei Live-TV (`VideoPlayer.Content(livetv)`) die tatsächliche EPG-Endzeit (`VideoPlayer.EndTime` bzw. `PVR.EpgEventFinishTime`) nutzt.
  - TopBar (`16x9/Includes_Furniture.xml`), PlayerControls und Video-OSD (`16x9/Includes_Window.xml`) sowie die RSS-Leiste (`16x9/Includes_Label.xml`) auf `Label_FinishTime`, `PVR.EpgEventElapsedTime`, `PVR.EpgEventDuration` und `PVR.EpgEventProgress` für Live-TV umgestellt.
- **Umstellung `DialogFavourites.xml` → `MyFavourites.xml` (Kodi 21+) & Debug-Overlay:**
  - Veraltete Datei `16x9/DialogFavourites.xml` entfernt (`16x9/MyFavourites.xml` wird ab Kodi 21 genutzt).
  - Verweise in `shortcuts/menus.xml`, `16x9/script-skinshortcuts-includes.xml` und `16x9/Custom_Overlay.xml` auf `MyFavourites` aktualisiert.
  - Nicht definierten Font `font13` und veraltete `<posx>`/`<posy>`-Koordinaten in `16x9/Custom_Overlay.xml` durch `Font-ListInfo` bzw. `<left>`/`<right>`/`<top>`/`<bottom>` ersetzt.

---

## 4. Migration auf `script.skinshortcuts` v3.0.4 (LibreELEC / Kodi 22)

- **`addon.xml`:**
  - Abhängigkeit von `<import addon="script.skinshortcuts" version="2.0.3" />` auf `version="3.0.4"` angehoben.
- **Neue v3-Konfigurationsdateien im Ordner `shortcuts/` erstellt (und veraltete v2-Dateien entfernt):**
  - `shortcuts/menus.xml`: Definiert `mainmenu`, `powermenu` sowie alle Hub-Menüs (`x1101` bis `x1119`), alle Standard-Einträge, Submenüs, Icon-Zuweisungen, Klick-Aktionen und benutzerdefinierte Gruppierungen (`mainmenu`, `hubs`, `commands`, `powermenu`).
  - `shortcuts/widgets.xml`: Definiert alle Widget-Gruppierungen, Standard-Widgets (Movies, TV Shows, Music, Weather, SimilarMovies, NextAired, Playlists) und Knotenpunkte.
  - `shortcuts/backgrounds.xml`: Definiert Standard-Hintergründe und Playlist-Hintergründe (`playlistBackground`).
  - `shortcuts/properties.xml`: Definiert die Button-Zuordnungen für den Verwaltungsdialog (`id="309"` Widget, `id="310"` Background, `id="9701"` Tile-Farbauswahl mit 24 Farbswatches, `id="9702"` PosterWidget-Toggle) sowie Fallback-/Standard-Properties.
  - `shortcuts/templates.xml`: Portiert die beiden Widget-Templates (`skinshortcuts-template-widget` und `skinshortcuts-template-submenu-widget`) auf das neue v3-Template-System (`<template type="menus">`, `<C9000>`, `<C9002>`, `<itemProperty>`, `<property>`).
  - Veraltete v2-Dateien (`overrides.xml`, `template.xml`, `mainmenu.DATA.xml`, `powermenu.DATA.xml`, `x1101.DATA.xml`, `x1102.DATA.xml`) entfernt.
- **Skript-Aufrufe (`RunScript(script.skinshortcuts,...)`) auf v3-Syntax umgestellt:**
  - `16x9/Home.xml`: `<onload>RunScript(script.skinshortcuts,type=buildxml)</onload>` (Komma-separiert; Menügruppen und IDs werden in v3 direkt aus `shortcuts/menus.xml` gelesen).
  - `16x9/SkinSettings.xml`: Doppeltes `<onunload>RunScript(...,type=buildxml...)</onunload>` entfernt (v3 baut das XML beim Schließen des Dialogs automatisch neu); Menü-Verwaltung auf `RunScript(script.skinshortcuts,type=manage,menu=mainmenu)` bzw. `menu=powermenu` umgestellt; Fallback-Widget-Auswahl auf `RunScript(script.skinshortcuts,type=skinstring,skinPath=home.fallbackwidget,skinLabel=home.fallbackwidget.name,skinType=home.fallbackwidget.type,skinTarget=home.fallbackwidget.target)` aktualisiert.
  - `16x9/Includes_Defs.xml`: Hub-Verwaltung (`Defs_Shortcuts_SetHub`) und Store-Widgets (`Defs_SkinSettings_StoreWidget`) auf `type=manage,menu=x$PARAM[hubid]` bzw. `type=skinstring,...` umgestellt.
- **Verwaltungsdialog `16x9/script-skinshortcuts.xml` an v3 angepasst:**
  - `Window.Property(groupname)` überall durch `Window.Property(menuname)` ersetzt.
  - Widget-Auswahlbutton von `id="312"` auf `id="309"` geändert (da `312` in v3 für „Eintrag zurücksetzen“ reserviert ist).
  - Neue v3-Buttons `id="311"` (Gelöschtes Element wiederherstellen), `id="312"` (Aktuelles Element auf Standard zurücksetzen) und `id="314"` (Gesamtes Menü zurücksetzen via `type=reset,menu=...`) integriert.
  - Entfernten Button `id="404"` (Custom Property Setter in v2) durch die native v3-Zuordnung in `shortcuts/properties.xml` für `id="9701"` (Tile-Farbe) und `id="9702"` (PosterWidget) abgelöst.
- **Geänderte Include-Namen und Item-Properties in v3 berücksichtigt:**
  - `16x9/Includes_Home.xml`: `<include>skinshortcuts-submenu</include>` → `<include>skinshortcuts-mainmenu-submenu</include>` sowie `ListItem.Property(action)` für Submenü-Klickbedingungen.
  - `16x9/DialogButtonMenu.xml`: `<include>skinshortcuts-group-powermenu</include>` → `<include>skinshortcuts-powermenu</include>`.
  - `16x9/Custom_Hub_1101.xml` bis `1119.xml`: `skinshortcuts-group-x1101` → `skinshortcuts-x1101` (alle 18 Hub-Dateien).
  - `16x9/Includes_Label.xml` & `16x9/Includes_Image.xml`: Neue v3-Properties `widgetLabel` (zusätzlich zu `widgetName`), `backgroundPath` (zusätzlich zu `Background`), `backgroundType=playlist` und `home.fallbackwidget.type=weather` ergänzt.

---

## 5. Vollständige Entfernung von `plugin.video.themoviedb.helper` (TMDbHelper)

- **Vollständige Entkopplung & native Kodi-Performance:**
  - Alle Abhängigkeiten zu `plugin.video.themoviedb.helper` wurden restlos aus dem Skin entfernt, um maximale Stabilität und Performance auf LibreELEC / Embedded-Systemen zu gewährleisten.
- **`addon.xml`:**
  - Das Add-on wurde komplett aus `<requires>` entfernt.
- **Kontextmenü (`16x9/DialogContextMenu.xml`):**
  - Veraltete TMDbHelper-Optionen (`id="997"` und `id="998"`) restlos entfernt.
- **Video-Infodialog (`16x9/DialogVideoInfo.xml`):**
  - Alle TMDb-spezifischen Buttons (Regisseur, InMovies, InTvShows, TMDb-Listen `id="9001"`–`id="9006"`) und die Container-Gruppe `id="9500"` entfernt.
  - Klick auf Darsteller (`id="51"`) führt nun direkt Kodis native Suche in der lokalen Medienbibliothek aus (`SendClick(2003,50)`).
- **Variablen & Includes (`Includes_Defs.xml`, `Includes_Furniture.xml`, `Includes_Image.xml`, `Includes_Label.xml`):**
  - Entfernung von `Defs_TMDBH_List_Content` und `Defs_TMDBH_List_Label`.
  - Entfernung aller `Window(Home).Property(TMDbHelper.*)`-Properties (Plot, Fanart, Top250, Awards, Rotten Tomatoes, Genre).
  - Alle Badges (z.B. Top250) und Beschreibungen greifen nun direkt und blitzschnell auf Kodis native Metadaten zu.
- **Einstellungen & Widgets (`16x9/SkinSettings.xml`, `shortcuts/widgets.xml`):**
  - Addon-Eintrag und Service-Monitor aus den Skin-Einstellungen entfernt.
  - TMDb-spezifische Widgets (`SimilarMovies`, `NextAired`) aus `shortcuts/widgets.xml` entfernt.

---

## 6. Integration von `plugin.program.autocompletion` (Virtuelle Tastatur)

- **`addon.xml`:**
  - `<import addon="plugin.program.autocompletion" version="2.1.2" optional="true" />` als optionale Abhängigkeit aufgenommen.
- **`16x9/Includes_Defs.xml` & `16x9/DialogKeyboard.xml`:**
  - Neue Variable `AutoCompletionContentVar` (analog zu Estuary mit `condition="System.AddonIsEnabled(plugin.program.autocompletion) + !System.HasHiddenInput"`) eingeführt, damit das Plugin nur abgefragt wird, wenn es installiert/aktiviert ist und kein Passwortfeld (`System.HasHiddenInput`) vorliegt.
  - Das im Skin bisher auskommentierte Vorschlags-Panel (`id="8000"`) sowie den erweiterten Dialog-Hintergrund in `16x9/DialogKeyboard.xml` aktiviert und die Navigation (`<onup>`/`<ondown>` zwischen Eingabezeile `312`, OK/Abbrechen `9001`, unterster Tastenreihe `5000` und Vorschlagsleiste `8000`) verknüpft.
- **`16x9/SkinSettings.xml`:**
  - Den bisher auskommentierten Eintrag für `plugin.program.autocompletion` (`id="8605"`) unter *Skin-Einstellungen → Add-ons* aktiviert (zum direkten Installieren bzw. Öffnen der Addon-Einstellungen).
