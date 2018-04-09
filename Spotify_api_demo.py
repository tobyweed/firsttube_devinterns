import sys
import spotipy
from flask import Flask, render_template, request
from spotipy.oauth2 import SpotifyClientCredentials

'''
https://open.spotify.com/embed?uri=spotify:artist:1JPy5PsJtkhftfdr6saN2i&theme=white&view=coverart
'''

artist_name = "Bassnectar"


client_credentials_manager = SpotifyClientCredentials(client_id='1cd3152f898243989589b4d05fd93e44', client_secret='fc69a8bc624743aea6c54d86616b22da')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search(q='artist:' + artist_name, type='artist')
try:
    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']
    related = sp.artist_related_artists(uri)
    onlyuri = []
    for artist in related['artists']:
        onlyuri.append(artist['uri'])
except:
    print("usage show_related.py [artist-name]")

a0 = onlyuri[0]
a1 = onlyuri[1]
a2 = onlyuri[2]
a3 = onlyuri[3]
a4 = onlyuri[4]


print(onlyuri)

print(a0)
print(a1)
print(a2)
print(a3)
print(a4)
