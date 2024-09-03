import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd 
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Credenciales desde las variables de entorno
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

nombre_artista = 'Imagine Dragons'
resultado = sp.search(q='artist: ' + nombre_artista, type='artist' )
artistas = resultado['artists']['items']
lista_artistas = []

for artista in artistas:
    nombre = artista['name']
    popularidad = artista['popularity']
    seguidores = artista['followers']['total']
    lista_artistas.append([nombre, popularidad, seguidores])
    
# Creación un dataframe

df_artistas = pd.DataFrame(lista_artistas, columns=['nombre', 'popularidad', 'seguidores'])
print(df_artistas)
