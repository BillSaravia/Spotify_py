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
    '37i9dQZEVXbOa2lmxNORXQ' : 'Colombia',
    '37i9dQZEVXbO3qyFxbkOE1' : 'Mexico',
    '37i9dQZEVXbL0GavIqMTeb' : 'Chile',
    '37i9dQZEVXbMMy2roB9myp' : 'Argentina',
    '37i9dQZEVXbJqfMFK4d691' : 'Bolivia',
    '37i9dQZEVXbMXbN3EUUhlg' : 'Brasil',
    '37i9dQZEVXbJlM6nvL1nD1' : 'Ecuador',
    '37i9dQZEVXbJfdy5b0KP7W' : 'Perú'
}

tracks_data = []

for playlist_id, country in playlists.items():
    results = sp.playlist_tracks(playlist_id)
    for i, item in enumerate(results['items']):
        track = item['track']
        tracks_info = {
            'Posición' : i + 1,
            'Nombre de la cación' : track['name'],
            'Artista(s)' : ', '.join([artist['name'] for artist in track['artists']]),
            'Popularidad' : track['popularity'],
            'País' : country  
        }
        tracks_data.append(tracks_info)
        
#creamos un dataframe 
df_tracks = pd.DataFrame(tracks_data)

query = """
Select * from df_tracks 
where País in ('Colombia', 'Mexico', 'Chile', 'Argentina', 'Brasil', 'Bolivia', 'Ecuador', 'Perú')
AND Posición IN (1, 2, 3)
Order by País, Posición
"""

top_3_sql = ps.sqldf(query, locals())

name_article = 'top_3_latinoamerica.csv'
top_3_sql.to_csv(name_article, index = False)


print (top_3_sql)