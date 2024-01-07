import json
from openpyxl import Workbook

INPUTFILE = 'data.json'
OUTPUTFILE = 'MuPiBox_MusikVerwaltung_Template_generated.xlsx'

documentation = [
    'x = Eintrag wird in data.json hinzugefügt',
    '',
    '',
    'Audibook und Music:',
    'Audibook und Music:',
    'Audibook und Music: Wert nur setzen, wenn aPartofAll = true ist',
    'Audibook und Music: Wert nur setzen, wenn aPartofAll = true ist',
    'Audibook und Music: Name für Album / Sammlung',
    'Audibook und Music: Artistid aus Spotify eines Künstlers',
    'Audibook: ID für Podcasts',
    'Audibook und Music: Spotify Query Syntax',
    'Audibook und Music: Attribut für "Menü Audibook und Music" -> "opt. Artist Cover"',
    'Audibook und Music: In diesem Attribut muss die ID eingetragen werden, wenn es sich um eine Playlist handelt',
    'Audibook und Music + Radio: AlbumID oder Stream Link',
    'Radio: Attribut für "Menü Radio" -> "Title". Ist der Titel für den Stream',
    'Radio: Attribut für "Menü Radio" -> "Cover Artwork URL"',
    'Interner Kommentar, welcher nicht in die data.json integriert wird',
    'Interner Kommentar, welcher nicht in die data.json integriert wird'
]
labels = ['add to file', 'type', 'category', 'shuffle', 'aPartOfAll', 'aPartOfAllMin', 'aPartOfAllMax', 'artist',
          'artistid', 'showid', 'query', 'artistcover', 'playlistid', 'id', 'title', 'cover', 'Kommentar', 'url']

wb = Workbook()
ws = wb.active

ws.append(documentation)
ws.append(labels)

with open(INPUTFILE, 'r', encoding='utf-8') as file:
    json_data = json.load(file)
    for json_entry in json_data:
        json_entry['add to file'] = 'x' # extend the dictionary with this field to generate an 'x' for this entry in the table
        table_entry = [json_entry.get(label, '') for label in labels] # if a label doesn't exist in the json_entry, the value defaults to ''
        ws.append(table_entry)
    wb.save(OUTPUTFILE)
