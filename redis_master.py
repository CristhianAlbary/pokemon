import json
from time import sleep
from redis import Redis
from rq import Queue
from redis_modules import get_pokemon

if __name__ == "__main__":
  print("Initializing redis master")
  redis_conn = Redis(host='127.0.0.1',port=6379)
  queue_jobs = Queue('busca', connection=redis_conn)
  jobs = []

  pokemons = []
  print("Digite os nomes de pokemons que dever ser consultados na api.")

  loop = True
  while(loop):
    pokeName = input("Digite o nome de um pokemon: ")
    pokemons.append(pokeName)
    print(pokeName + "Adicionado a lista.")

    input_s = input("Deseja adicionar mais nomes? s para sim")

    if(input_s != "s"):
      loop = False

  print(pokemons)

  for pokemon in pokemons:
    job = queue_jobs.enqueue(get_pokemon, pokemon)
    jobs.append(job)

  for job in jobs:
    print("Buscas enfileiradas {0}".format(len(queue_jobs)))
    while job.result is None:
      print("A busca {0} ainda nao foi concluido".format(job.id))
      sleep(2)
      print("Resultado {0}".format(job.result))
    print(job.result)
