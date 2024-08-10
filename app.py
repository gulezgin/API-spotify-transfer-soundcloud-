import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

# Spotify API bilgileri
SPOTIPY_CLIENT_ID = 'c26cbdc3d49747***'
SPOTIPY_CLIENT_SECRET = '5ec4ea***'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# SoundCloud API bilgileri
SOUNDCLOUD_AUTH_TOKEN = '2-29***-3473***-c3axJ***'

# Spotify API ile bağlantı kurma
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-read-private"
))

# Çalma listesi ID'si
playlist_id = '3y8***'

# Çalma listesi bilgilerini alma
playlist = sp.playlist_tracks(playlist_id)

tracks = playlist['items']
for track in tracks:
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    print(f'Track: {track_name}, Artist: {artist_name}')

    # SoundCloud'a şarkı ekleme
    headers = {
        'Authorization': f'OAuth {SOUNDCLOUD_AUTH_TOKEN}',
        'Content-Type': 'application/json'
    }

    # Ses dosyasını yükleme işlemi için uygun endpoint ve veri eklenmelidir
    data = {
        'title': track_name,
        'description': f'Song by {artist_name}'
        # 'asset_data': 'path_to_your_audio_file.mp3'  # Ses dosyası gerekmektedir
    }

    response = requests.post('https://api.soundcloud.com/tracks', headers=headers, json=data)

    if response.status_code == 201:
        print(f'Successfully added: {track_name}')
    else:
        print(f'Failed to add: {track_name}. Status code: {response.status_code}, Response: {response.text}')
