# Instructions:
# ============
# - Run this file as script;
# - The web browser will open and spotify will ask to grant access;
# - After proceeded, the script will prompt to insert the full url where you've
#   redirect to;
# - Don't forget to set the same `redirect_uri` on the developers dashboard
#   configuration.

import os

from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")

oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-read-private playlist-modify-private",
)

print(oauth)
