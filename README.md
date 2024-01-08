# MuPiBox_MusikVerwaltung
Verwaltung der Medienbibliothek der MuPiBox (https://mupibox.de/) in einer Excel Tabelle

## Zielsetzung
Mit den Python Skripten in diesem repo kann die Medienbibliothek der MuPiBox in einer Excel Tabelle verwaltet werden.

Das Skript `MuPiBox-MusikVerwaltung-json2xlsx.py` generiert auf Basis der `data.json` Datei der
MuPiBox eine Excel Tabelle, in der dann die Medienbibliothek verwaltet werden kann. Nachdem in der Tabelle
Einträge editiert, hinzugefügt oder gelöscht wurden, wird mit dem Skript `MuPiBox-MusikVerwaltung-xlsx2json.py`
aus der Excel Tabelle die aktualisierte `data.json` Datei generieren, die dann wieder auf die MuPiBox kopiert wird.

## Vorraussetzung
- Aktuelle Python Version installieren (https://www.python.org/)
- openpyxl installieren (Folgenden Befehl auf der Konsole eingeben: ```pip install openpyxl```)
- SSH Verbindungsdaten der MuPiBox siehe https://mupibox.de/anleitungen/einstellungen/schnellzugriff-passwoerter/)
- Aktivierter FTP oder Samba Server auf der MuPiBox, um Dateien zu transferieren (siehe http://mupibox/network.php > Services)

## Excel Dokument aus data.json generieren
- SSH Verbindung zur Mupibox aufbauen und die `data.json` in den File Exchange Ordner kopieren: ```cp /home/dietpi/.mupibox/Sonos-Kids-Controller-master/server/config/data.json /home/dietpi/MuPiBox/data.json```
- `data.json` via FTP oder Samba von der Mupibox auf den Rechner in den Ordner mit dem Converter Skripten kopieren
- Das Python Skript `MuPiBox-MusikVerwaltung-json2xlsx.py` ausführen (z.B. in VSCode im Terminal mit dem Befehl ```python .\MuPiBox-MusikVerwaltung-json2xlsx.py```)
- Die Medienbibliothek in der Excel Tabelle verwalten (Einträge hinzufügen, löschen, editieren).
- Anschließend die aktualisierte `data.json` Datei exportieren und auf die MuPiBox kopieren (siehe nächster Abschnitt)

## data.json aus dem Excel Dokument generieren
- Sicherstellen, dass das Excel Dokument und Pythonskript im selben Ordner liegen
- Wenn die Excel Datei umbenannt wurde, muss der Dateiname auch im Skript geändert werden (https://github.com/Feuer-sturm/MuPiBox_MusikVerwaltung/blob/515d3d6e02c7477e89f033842d04a717e37a0b9b/MuPiBox-MusikVerwaltung-xlsx2json.py#L5)
- Das Python Skript `MuPiBox-MusikVerwaltung-xlsx2json.py` ausführen (z.B. in VSCode im Terminal mit dem Befehl ```python .\MuPiBox-MusikVerwaltung-xlsx2json.py```)
- `data.json` wird generiert
- `data.json` via FTP oder Samba auf die Mupibox kopieren
- SSH Verbindung zur Mupibox aufbauen und die `data.json` an den korrekten Zielort kopieren: ```cp /home/dietpi/MuPiBox/data.json /home/dietpi/.mupibox/Sonos-Kids-Controller-master/server/config/data.json```
- Auf der MuPiBox Oberfläche zwischen Musik/Hörbuch/Radio wechseln, so dass die `data.json` neu geladen wird. Notfalls die MuPiBox einmal neustarten.

## How to transfer files via FTP on a Mac
- open a terminal
- switch to the folder where `data.json` is stored (usually the root folder of this repo)
- run `ftp mupibox` and enter the credentials (see https://mupibox.de/anleitungen/einstellungen/schnellzugriff-passwoerter/)
- run `put data.json`
- The file is transferred to the File Exchange folder of the MuPiBox

## Änderungshistorie
v1.0 (2024-01-05)
- Initiale Version

v1.1 (2024-01-07)
- json2xlsx Converter hinzugefügt
