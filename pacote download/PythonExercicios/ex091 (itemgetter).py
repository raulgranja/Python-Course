from random import randint
from operator import itemgetter
from time import sleep
n = {'jogador1': randint(1, 6),
     'jogador2': randint(1, 6),
     'jogador3': randint(1, 6),
     'jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in n.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.75)
ranking = sorted(n.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
