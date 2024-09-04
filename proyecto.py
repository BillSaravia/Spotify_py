import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd 
import pandasql as ps
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Credenciales desde las variables de entorno
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


playlists = {
    # '37i9dQZF1Fa1IIVtEpGUcU' : 'Playlist 2023',
    '37i9dQZF1E35NFuZr3uZ6z' : 'Mix 2 Anime op',
    '37i9dQZF1E35ykA6hH2cus' : 'Mix 6 AMV'
    
}

tracks_data = []

#iteramos sobre cada playlist

for playlist_id, album in playlists.items():
    results = sp.playlist_tracks(playlist_id)
    for i, item in enumerate(results['items']):
        track = item['track']
        track_info = {
            'posición': i + 1,
            'Nombre de la canción': track['name'],
            'Artista(s)': ', '.join([artist['name'] for artist in track['artists']]),
            'Popularidad': track['popularity'],
            'Álbum':album
        } 
        tracks_data.append(track_info)
        
# crear detaframe
df_tracks = pd.DataFrame(tracks_data)
# df_tracks.to_csv('top_tracks_music_rquagmire.csv', index = False)

query = """
select * from df_tracks 
where Álbum In ('Mix 2 Anime op', 'Mix 6 AMV')
And posición in (1,2,3,4,5)
order by Álbum, posición
Limit 10
"""
top_5_sql = ps.sqldf(query,locals())
print(top_5_sql)


        