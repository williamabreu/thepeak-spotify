import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
playlist_id = os.environ.get("SPOTIFY_PLAYLIST_ID")

spotify = spotipy.Spotify(
    oauth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-read-private playlist-modify-private",
        open_browser=False,
    )
)

# Clean the playlist and insert the news tracks.

# TODO: Convert to a for loop, each request is limited to 100
tracks = spotify.playlist_items(playlist_id=playlist_id)
items = [x["track"]["id"] for x in tracks["items"]]

res = spotify.playlist_remove_all_occurrences_of_items(
    playlist_id=playlist_id,
    items=items,
)

res = spotify.playlist_add_items(
    playlist_id=playlist_id,
    items=["0brBOx8ejPXvBYnQkWquYK", "2RsAajgo0g7bMCHxwH3Sk0"],
)

print(res)
