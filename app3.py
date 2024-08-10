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

# Çalma listesi oluşturma
playlist_data = {
    'title': 'My Spotify Playlist',
    'description': 'A playlist imported from Spotify',
}

headers = {
    'Authorization': f'OAuth {SOUNDCLOUD_AUTH_TOKEN}',
    'Content-Type': 'application/json',
}

response = requests.post('https://api.soundcloud.com/playlists', headers=headers, json=playlist_data)

if response.status_code == 201:
    print('Playlist created successfully')
    playlist_id = response.json()['id']
else:
    print(f'Failed to create playlist. Status code: {response.status_code}, Response: {response.text}')

# Şarkı ekleme (Bu örnek varsayımsaldır, SoundCloud API'sinde çalma listesine şarkı eklemek desteği bulunmayabilir)
for track in tracks:
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    print(f'Attempting to add track: {track_name} by {artist_name}')

    # Ses dosyasını yükleme işlemi yapılmalıdır
    data = {
        'title': track_name,
        'description': f'Song by {artist_name}',
        # 'asset_data': 'path_to_your_audio_file.mp3'  # Ses dosyası yolu gerekmektedir
    }

    response = requests.post(f'https://api.soundcloud.com/playlists/{playlist_id}/tracks', headers=headers, json=data)

    if response.status_code == 201:
        print(f'Successfully added: {track_name}')
    else:
        print(f'Failed to add: {track_name}. Status code: {response.status_code}, Response: {response.text}')
