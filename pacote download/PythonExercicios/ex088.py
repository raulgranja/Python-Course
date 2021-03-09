from random import randint
from time import sleep
print('-' * 30)
print('      JOGA NA MEGA SENA       ')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=- SORTEANDO {n} JOGOS -=-=-')
r = randint(1, 60)
M = []
for i in range(n):
    L = []
    for j in range(6):
        while r in L:
            r = randint(1, 60)
        L.append(r)
    L.sort()
    print(f'Jogo {i + 1}: {L}')
    sleep(0.7)
    M.append(L)
print('Boa sorte!')
