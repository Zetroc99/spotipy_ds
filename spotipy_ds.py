import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
"""
export SPOTIPY_CLIENT_ID='1746dbf63fa84b4095f88aa11df2eda2'
export SPOTIPY_CLIENT_SECRET='4e0ae57d50be40238cff2a9ef16e31fd'
export SPOTIPY_REDIRECT_URI='http://localhost'
"""

weeknd = '1Xyo4u8uXC1ZmMpatF05PJ'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(weeknd, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

#spotify.current_user_top_tracks()