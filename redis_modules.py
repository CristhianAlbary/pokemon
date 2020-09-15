import json
import requests
from time import sleep

def get_pokemon(pokemonName):
  sleep(2)
  response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemonName).json()
  data = {
    'codigo':response["id"],
    'name':response["name"],
    'order':response["order"]
  }
  return data
