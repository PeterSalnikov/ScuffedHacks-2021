# SCUFFED HACKS 2021

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

target = sp.playlist_items(playlist_id='4gKMgvqgoB3j09i3J4Akhx?si=655b7f9d1c324f3f', fields='tracks,next')

# create list from tracks on playlist with format "ARTIST NAME"
def save_tracks(playlist):
    artist_track_list = []
    for i, item in enumerate(playlist['items']):
        track = item['track']
        artist_track_list.append(track['artists'][0]['name'] + " " + track['name'])
    return artist_track_list


tracks = target['tracks']

track_list = save_tracks(tracks)

df = pd.DataFrame(track_list, columns=["tracks"])
df.to_csv('track_list.csv', index=False)