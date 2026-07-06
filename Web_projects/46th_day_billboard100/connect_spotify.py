import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Thank you Spotify for changing you API and making it limited and complicated and making Spotipy obsolete
# 

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)
# Create a Spotify Client
# AUTHORIZATION SCOPES: https://developer.spotify.com/documentation/general/guides/scopes/
 
# Get current user details

def create_playlist(name, description="", public=False):
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(
        user=user_id,
        name=name,
        public=public,
        description=description
    )
    return playlist["id"]

def find_track_uri(song_name, artist_name):
    query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=query, type="track", limit=1)
    items = results["tracks"]["items"]
    if not items:
        # Fallback: looser search without field filters
        results = sp.search(q=f"{song_name} {artist_name}", type="track", limit=1)
        items = results["tracks"]["items"]
    if not items:
        print(f"⚠️ Not found: {song_name} - {artist_name}")
        return None
    return items[0]["uri"]

def add_songs_to_playlist(playlist_id, songs):
    """
    songs: list of (song_name, artist_name) tuples
    """
    uris = []
    for song_name, artist_name in songs:
        uri = find_track_uri(sp, song_name, artist_name)
        if uri:
            uris.append(uri)

    # Spotify API allows max 100 tracks per request
    for i in range(0, len(uris), 100):
        sp.playlist_add_items(playlist_id, uris[i:i+100])

    return uris