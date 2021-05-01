# SCUFFED HACKS 2021

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

target = sp.playlist_items(playlist_id='4gKMgvqgoB3j09i3J4Akhx?si=655b7f9d1c324f3f', fields='tracks,next')


def save_tracks(results):
    tracks_artists = []
    for i, item in enumerate(results['items']):
        track = item['track']
        tracks_artists.append(track['artists'][0]['name'] + " " + track['name'])
    return tracks_artists


tracks = target['tracks']

list = save_tracks(tracks)
print(list)

df = pd.DataFrame(list, columns=["tracks"])
df.to_csv('tracklist.csv', index=False)