# SCUFFED HACKS 2021

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

scope = "user-library-read"
#
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

target = sp.playlist_items(playlist_id='4gKMgvqgoB3j09i3J4Akhx?si=655b7f9d1c324f3f', fields='tracks,next')


def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        print(
            "   %d %32.32s %s" %
            (i, track['artists'][0]['name'], track['name']))


tracks = target['tracks']

# print(target['name'])

show_tracks(tracks)

# print(target['tracks']['name'])
# df = pd.DataFrame(target)

# print(df.to_string())
