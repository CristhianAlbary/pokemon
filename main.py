import json
import requests
var = 'bulbasaur'
api_url = 'https://pokeapi.co/api/v2/pokemon/' + var

data = requests.get(api_url)

print(data.content)