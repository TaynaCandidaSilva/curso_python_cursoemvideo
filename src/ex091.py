from operator import itemgetter
from time import sleep
from random import randint

jogo = {'jogador1': randint(1, 6),
      'jogador2': randint(1, 6),
      'jogador3' : randint(1, 6),
      'jogador4' : randint(1, 6)}
ranking = list()

print(f'VALORES SORTEADOS:')
for k, v in jogo.items():
      print(f'{k} tirou {v} no dado') 
      sleep(1)   
print('=-'*20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('     == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
      print(f"    - O {i+1}° lugar: {v[0]} com {v[1]}")
      sleep(1)
      



