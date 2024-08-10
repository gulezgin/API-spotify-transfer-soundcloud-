import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

# Spotify API bilgileri
SPOTIPY_CLIENT_ID = '***'
SPOTIPY_CLIENT_SECRET = '***'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# SoundCloud API bilgileri
SOUNDCLOUD_AUTH_TOKEN = '***'
SOUNDCLOUD_CLIENT_ID = '***'

# Spotify API ile bağlantı kurma
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-read-private"
))

# Çalma listesi ID'si
spotify_playlist_id = '***'

# Spotify'dan çalma listesi bilgilerini alma
playlist = sp.playlist_tracks(spotify_playlist_id)
tracks = playlist['items']

# SoundCloud'da çalma listesi oluşturma
def create_soundcloud_playlist(name, description):
    headers = {
        'Authorization': f'OAuth {SOUNDCLOUD_AUTH_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'title': name,
        'description': description,
        'sharing': 'public'
    }
    response = requests.post('https://api.soundcloud.com/playlists', headers=headers, json=data)
    if response.status_code == 201:
        return response.json()['id']
    else:
        raise Exception(f'Failed to create playlist. Status code: {response.status_code}, Response: {response.text}')

# SoundCloud'da şarkı arama
def search_soundcloud_track(query):
    headers = {
        'Authorization': f'OAuth {SOUNDCLOUD_AUTH_TOKEN}'
    }
    params = {
        'q': query,
        'limit': 1
    }
    response = requests.get('https://api.soundcloud.com/tracks', headers=headers, params=params)
    if response.status_code == 200:
        tracks = response.json()
        if tracks:
            return tracks[0]['id']
    return None

# Çalma listesine şarkı ekleme
def add_track_to_soundcloud_playlist(playlist_id, track_id):
    headers = {
        'Authorization': f'OAuth {SOUNDCLOUD_AUTH_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'track_id': track_id
    }
    response = requests.post(f'https://api.soundcloud.com/playlists/{playlist_id}/tracks', headers=headers, json=data)
    if response.status_code == 201:
        print(f'Successfully added track ID {track_id} to playlist ID {playlist_id}')
    else:
        print(f'Failed to add track ID {track_id} to playlist ID {playlist_id}. Status code: {response.status_code}, Response: {response.text}')

# Yeni bir çalma listesi oluştur
playlist_name = 'New Playlist from Spotify'
playlist_description = 'This playlist was created from Spotify tracks.'
try:
    soundcloud_playlist_id = create_soundcloud_playlist(playlist_name, playlist_description)
    print(f'Created SoundCloud playlist ID: {soundcloud_playlist_id}')

    # Spotify'daki şarkıları al ve SoundCloud'da arat
    for track in tracks:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        query = f'{track_name} {artist_name}'
        print(f'Searching for: {query}')
        track_id = search_soundcloud_track(query)
        if track_id:
            add_track_to_soundcloud_playlist(soundcloud_playlist_id, track_id)
        else:
            print(f'Track not found on SoundCloud: {query}')
except Exception as e:
    print(str(e))
