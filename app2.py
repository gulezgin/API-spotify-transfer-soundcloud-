
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API bilgileri
SPOTIPY_CLIENT_ID = 'c26cbdc3d49747fda239d5add421b533'
SPOTIPY_CLIENT_SECRET = '5ec4ea0331014f879a7b6263042c415b'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Spotify API ile bağlantı kurma
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-read-private"
))

# Çalma listesi ID'si
playlist_id = '3y8JUgHStIHbaTx54vtlnI'

# Çalma listesi bilgilerini alma
playlist = sp.playlist_tracks(playlist_id)

tracks = playlist['items']
for track in tracks:
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    print(f'Track: {track_name}, Artist: {artist_name}')
import requests

# SoundCloud API bilgileri
SOUNDCLOUD_AUTH_TOKEN = '2-296399-347324420-c3axJHGtf2ugpK'

# Ses dosyasının yolu
track_file_path = 'C:/Users/msı/Music.mp3'  # Gerçek dosya yolunu buraya yazın

try:
    with open(track_file_path, 'rb') as f:
        # SoundCloud'a şarkı ekleme
        headers = {
            'Authorization': f'OAuth {SOUNDCLOUD_AUTH_TOKEN}'
        }

        # Multipart form-data formatında veri hazırlama
        files = {
            'track[title]': (None, 'Track Title'),  # Track title burada verilmelidir
            'track[asset_data]': (track_file_path, f, 'audio/mpeg')
        }

        response = requests.post('https://api.soundcloud.com/tracks', headers=headers, files=files)

        if response.status_code == 201:
            print('Successfully added the track to SoundCloud.')
        else:
            print(f'Failed to add the track. Status code: {response.status_code}, Response: {response.text}')
except FileNotFoundError:
    print(f'File not found: {track_file_path}')
