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
- Wenn die Excel Datei umbenannt wurde, muss der Dateiname auch im Skript geändert werden (https://github.com/Feuer-sturm/MuPiBox_MusikVerwaltung/blob/a988f7b8d7183b2c2acdfb834b99b186f8e15006/MuPiBox-MusikVerwaltung-xlsx2json.py#L5)
- Das Python Skript `MuPiBox-MusikVerwaltung-xlsx2json.py` ausführen (z.B. in VSCode im Terminal mit dem Befehl ```python .\MuPiBox-MusikVerwaltung-xlsx2json.py```)
- `data.json` wird generiert
- `data.json` via FTP oder Samba auf die Mupibox kopieren
- SSH Verbindung zur Mupibox aufbauen und die `data.json` an den korrekten Zielort kopieren: ```cp /home/dietpi/MuPiBox/data.json /home/dietpi/.mupibox/Sonos-Kids-Controller-master/server/config/data.json```
- Auf der MuPiBox Oberfläche zwischen Musik/Hörbuch/Radio wechseln, so dass die `data.json` neu geladen wird. Notfalls die MuPiBox einmal neustarten.
- Wenn ihr noch lokale Musik auf der Mupibox habt, dann müsst über die MuPiBox Admin Seite -> Reiter Admin -> Menü "Music database" das "Clean and update music database" noch einmal anstoßen, damit die lokale Musik wieder zur internen data.json hinzugefügt wird

## data.json via FTP vom Mac auf die MuPiBox übertragen
- Terminal öffnen
- in das Verzeichnis wechseln, in dem `data.json` liegt (normalerweise im root Verzeichnis von diesem repo)
- `ftp mupibox` auf dem Terminal ausführen und die Logindaten für den FTP Server eingeben (siehe https://mupibox.de/anleitungen/einstellungen/schnellzugriff-passwoerter/)
- `put data.json` auf dem Terminal ausführen, um `data.json` auf die MuPiBox zu kopieren
- den FTP Client mit `quit` beenden

## Änderungshistorie
v1.2 (2024-07-14)
- Attribute für Mupibox Version 4.0.4 angepasst, Template Excel Datei aktualisiert, Spaltenbezeichnung vereinheitlicht

v1.1 (2024-01-07)
- json2xlsx Converter hinzugefügt

v1.0 (2024-01-05)
- Initiale Version


