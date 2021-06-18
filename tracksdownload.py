from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import requests
import os


# Verbindung mit Spotify API durch meine client_id und meine client_secret:

client_credentials_manager = SpotifyClientCredentials(client_id= '38e9a036557b4866822c8a0ace872f8e', client_secret= 'e83625f29c194311ba237eafda54e558')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# anfordern der Daten von der Playlist (playlist_id ist der Spotify URL beim kopieren in der app)

playlist_id = 'spotify:playlist:5L1xosSKARKvCD5jMNaJwm'
playlistdaten = sp.playlist(playlist_id)

"""
Aufbau der Daten die ich bekomme (playlistdaten):
{
    "tracks": {
        "items": [
            "track": {
               "preview_url": ........ ,
            }
        ]
    }
}

Die nächsten Zeilen schrieben die links in eine Liste und sortieren dann noch die items ohne link drin raus.
link_2 ist die fertige Liste
"""

links_1 = []
for x in playlistdaten["tracks"]["items"]:
    links_1.append(x["track"]["preview_url"])

print(links_1)
print("Länge links_1:", str(len(links_1)))

links_2 = list(filter(None, links_1))

print(links_2)
print("Länge links_2:", str(len(links_2)))


# Die nächten Zeilen laden die preview tracks vom jeweiligen link herunter.
pfad = '../daten/edm/'
genre = 'edm'
nummer = 0

for x in links_2:
    myfile = requests.get(links_2[nummer])
    open(pfad + genre + str(nummer) + '.mp3', 'wb').write(myfile.content)
    nummer += 1


