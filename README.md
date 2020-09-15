# Como utilizar:
Este este projeto possui dois scripts principais e um auxiliar.

* redis_modules.py - Possui a implementação de métodos que serão utilizados no master e workers;
* redis_master.py - Script que executa o processo principal, que adiciona trabalhos em uma fila, e aguarda os seus resultados. Também conecta-se em um servidor Redis, obrigatório e necessário para controle local ou externo das filas.
* redis_worker.py - Implementa a execução dos trabalhos que estão disponíveis em fila, sendo necessário conexão com o mesmo Redis do processo principal. Pode executar multíplas instâncias deste script localmente ou em diversas máquinas remotas.

## Executar nas maquinas(tanto em worker(s) quanto na master).
```
worker$ cd ~ && git clone https://github.com/fabiosammy/python_redis_multiprocess.git
worker$ sudo apt-get update
worker$ sudo apt-get install python-pip python-redis
worker$ sudo pip install rq
worker$ cd ~/python_redis_multiprocess/
```

#### Verifiquem se o redis esta rodando na maquina master(ou outra exclusiva para tal).
```
master$ docker run --rm --network="host" -p 6379:6379 redis:3.2-alpine
```

#### Agora alterem o arquivo `redis_worker` afim de apontar o serviço redis para o ip da maquina que está executando o serviço redis.
```
worker$ python redis_worker.py
```

#### E por fim, caso estejam rodando o redis na mesma máquida que o master, somente executem o script. Caso contrário, alterem devidamente o script afim de apontar para o ip correto. 
```
master$ python redis_master.py
```

$ pip install requests

pokemons = ['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raticate', 'spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash', 'nidoran', 'nidorina', 'nidoqueen', 'nidoran', 'nidorino', 'nidoking', 'clefairy', 'clefable', 'vulpix', 'ninetales', 'jigglypuff', 'wigglytuff', 'zubat', 'golbat', 'oddish', 'gloom', 'vileplume', 'paras', 'parasect', 'venonat', 'venomoth', 'diglett', 'dugtrio', 'meowth', 'persian', 'psyduck', 'golduck', 'mankey', 'primeape', 'growlithe', 'arcanine', 'poliwag', 'poliwhirl', 'poliwrath', 'abra', 'kadabra', 'alakazam', 'machop', 'machoke', 'machamp', 'bellsprout', 'weepinbell', 'victreebel', 'tentacool', 'tentacruel', 'geodude', 'graveler', 'golem', 'ponyta', 'rapidash', 'slowpoke', 'slowbro', 'magnemite', 'magneton', 'farfetch', 'doduo', 'dodrio', 'seel', 'dewgong', 'grimer', 'muk', 'shellder', 'cloyster', 'gastly', 'haunter', 'gengar', 'onix', 'drowzee', 'hypno', 'krabby', 'kingler', 'voltorb', 'electrode', 'exeggcute', 'exeggutor', 'cubone', 'marowak', 'hitmonlee', 'hitmonchan', 'lickitung', 'koffing', 'weezing', 'rhyhorn', 'rhydon', 'chansey', 'tangela', 'kangaskhan', 'horsea', 'seadra', 'goldeen', 'seaking', 'staryu', 'starmie', 'scyther', 'jynx', 'electabuzz', 'magmar', 'pinsir', 'tauros', 'magikarp', 'gyarados', 'lapras', 'ditto', 'eevee', 'vaporeon', 'jolteon', 'flareon', 'porygon', 'omanyte', 'omastar', 'kabuto', 'kabutops', 'aerodactyl', 'snorlax', 'articuno', 'zapdos', 'moltres', 'dratini', 'dragonair', 'dragonite', 'mewtwo', 'mew'] 

############################# Ideias ###########################

Conferir os resultados do json para chegamos a um resultados mais enxuto.

Entrada de dados do usário para interação com sistema.

    Pedir para o usuário passar o nome do pokemon para fazer a pesquisa.

Implementar duas filas uma pega o parametro e outra executar a função de requisição na API.
