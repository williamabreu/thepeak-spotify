import json
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

spotify = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
)

results = spotify.search("Cold War Kids What you say", limit=1)

with open("spotipy.json", "w") as fp:
    json.dump(results, fp, indent=2)

print("id =", results["tracks"]["items"][0]["id"])
print("uri =", results["tracks"]["items"][0]["uri"])
