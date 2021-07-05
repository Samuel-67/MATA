import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id= '38e9a036557b4866822c8a0ace872f8e', client_secret= 'e83625f29c194311ba237eafda54e558')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = '65fr1aWmt2kdHNXzu4CqRD'
playlistdaten = sp.playlist_tracks(playlist_id, offset=0)

print(playlistdaten['total'])
print(type(playlistdaten['total']))
