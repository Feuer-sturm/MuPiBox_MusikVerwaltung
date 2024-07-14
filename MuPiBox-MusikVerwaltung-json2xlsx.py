import json
from openpyxl import Workbook

INPUTFILE = 'data.json'
OUTPUTFILE = 'MuPiBox_MusikVerwaltung_Template.xlsx'

documentation = [
    'x = Eintrag wird in data.json hinzugefügt',
    '',
    '',
    'nur bei category music + other nutzbar:',
    'nur bei type spotify + rss nutzbar:',
    'Wert nur setzen, wenn aPartofAll = true ist',
    'Wert nur setzen, wenn aPartofAll = true ist',
    'Name für Album / Sammlung (type = Spotify, Radio, RSS):',
    'Album Cover',
    'Label Cover',
    'Spotify Query Syntax (type = spotify)',
    'Spotify URL (type = spotify)',
    'Artist ID aus Spotify URL, Artist ID NUR füllen wenn alles vom Artist geladen werden soll (type = spotify)',
    'Playlist ID aus Spotify URL, type = spotify',
    'ID für type = Radio + RSS + spotify (Album ID aus Spotify URL, ID ausfüllen, wenn es sich um ein einzelnes Album handelt)',
    'Titel für Radio/Stream (type Radio/Stream)' ,
    'Interner Kommentar, welcher nicht in die data.json integriert wird',
    'Interner Kommentar, welcher nicht in die data.json integriert wird'
]
labels = ['add to file', 'type', 'category', 'shuffle', 'aPartOfAll', 'aPartOfAllMin', 'aPartOfAllMax', 'artist',
          'artistcover', 'cover', 'query', 'spotify_url', 'artistid', 'playlistid', 'id', 'title', 'Kommentar', 'url']

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
