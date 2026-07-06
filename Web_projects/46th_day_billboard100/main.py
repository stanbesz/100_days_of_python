from pprint import pprint

from bakeboard_data import FALLBACK_DATE,collect_bakeboard_data,create_song_map,date_logic
from connect_spotify import create_playlist,sp,add_songs_to_playlist,find_track_uri

# Collect bakeboard information
date = date_logic()
bakeboard_data = collect_bakeboard_data(date)
song_map = create_song_map(bakeboard_data[1])

# connect to Spotify and create playlist
date = date.strftime('%Y-%m-%d/') if bakeboard_data[0] else FALLBACK_DATE  # Use the valid date if available, otherwise fallback
playlist_id = create_playlist(date+" :Top 100 Bakeboard", "Made with Spotipy")
added_uris = add_songs_to_playlist(playlist_id, song_map)
pprint(song_map)
