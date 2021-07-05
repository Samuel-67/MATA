import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import math
import requests

client_credentials_manager = SpotifyClientCredentials(client_id= '38e9a036557b4866822c8a0ace872f8e', client_secret= 'e83625f29c194311ba237eafda54e558')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = '6MXkE0uYF4XwU4VTtyrpfP'
playlist = sp.playlist_tracks(playlist_id) # playlist einmal laden um die Anzahl tracks zu bekommen ('total')

durchgaenge = math.ceil(playlist['total']/100) # wie oft soll der unter for loop gemacht werden (anzahl tracks durch hundert, weil pro durchgang 100 tracks gedownloadet werden). ist gerundet auf die nächst höhere gnaze zahl, damit auch wenn es nur noch 6 tracks sind noch ein durchgang gemacht wird
offset = 0
p = 0
nummer = 0

pfad = '../daten/hiphop/'
genre = 'hiphop'

for i in range (int(durchgaenge)):
    playlistdaten = sp.playlist_tracks(playlist_id, offset=offset)

    links_1 = []
    for x in playlistdaten["items"]:
        links_1.append(x["track"]["preview_url"])


    links_2 = list(filter(None, links_1))
    p += len(links_2)

    offset += 100

    n= 0
    # Die nächten Zeilen laden die preview tracks vom jeweiligen link herunter.
    for x in links_2:
        myfile = requests.get(links_2[n])
        open(pfad + genre + str(nummer) + '.mp3', 'wb').write(myfile.content)
        nummer += 1
        n += 1

print(p) #wie viele tracks habe ich die ich herunterladen kann