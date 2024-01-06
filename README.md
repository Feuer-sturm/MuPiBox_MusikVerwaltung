# MuPiBox_MusikVerwaltung
Musik Verwaltung Excel2Json für die MuPiBox (https://mupibox.de/)

## Zielsetzung
Mit diesem Skript kann die Musikverwaltung für die MuPiBox in einer Excel Datei durchgeführt werden. Auf Basis der Excel Datei wird die für die MuPiBox notwendige data.json Datei generiert, welche dann nur noch auf die MuPiBox kopiert werden muss.

## Vorraussetzung
- Aktuelle Python Version installieren (https://www.python.org/)
- openpyxl installieren (Folgenden Befehl auf der Konsole eingeben: ```pip install openpyxl```)
- SSH Verbindungsdaten der MuPiBox siehe https://mupibox.de/anleitungen/einstellungen/schnellzugriff-passwoerter/)



## data.json aus dem Excel Dokument generieren
- Excel Dokument und Pythonskript im selben Ordner ablegen
- Musik für die MuPiBox im Excel Dokument verwalten und speichern
- Wenn Excel Datei umbenannt wird, muss der Dateiname hier im Skript geändert werden: https://github.com/Feuer-sturm/MuPiBox_MusikVerwaltung/blob/515d3d6e02c7477e89f033842d04a717e37a0b9b/MuPiBox-MusikVerwaltung-xlsx2json.py#L5
- Python Skript ausführen (z.B. in VSCode im Terminal mit dem Befehl ```py .\MuPiBox-MusikVerwaltung-xlsx2json.py```)
- data.json wird generiert
- data.json z.B. via FTP auf die Mupibox kopieren
- SSH Verbindung zur Mupibox aufbauen und die data.json an den korrekten Zielort kopieren: ```cp /home/dietpi/MuPiBox/data.json /home/dietpi/.mupibox/Sonos-Kids-Controller-master/server/config/data.json```
- In der Regel reicht es aus, auf der MuPiBox Oberfläche zwischen Musik, Hörbuch, Radio zu wechseln, so dass die neue data.json geladen wird. Notfalls die MuPiBox einmal neustarten
- Wenn ihr noch lokale Musik auf der Mupibox habt, dann müsst über die MuPiBox Admin Seite -> Reiter Admin -> Menü "Music database" das "Clean and update music database" noch einmal anstoßen, damit die lokale Musik wieder zur internen data.json hinzugefügt wird


## Änderungshistorie
v1.0 (2024-01-05)
- Initiale Version

