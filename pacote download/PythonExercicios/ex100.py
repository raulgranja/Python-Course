from random import randint
from time import sleep


def sorteia(L):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        sleep(0.3)
        n = randint(0, 10)
        L.append(n)
        print(n, end=' ')
    print('PRONTO!')


def somaPar(L):
    soma = 0
    for i in L:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {L}, temos {soma}')


lista = []
sorteia(lista)
somaPar(lista)
