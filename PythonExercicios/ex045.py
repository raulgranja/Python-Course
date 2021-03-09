from random import randint
from time import sleep

print('\033[1:36m-=-\033[m' * 20)
print('\033[33mJOKENPÔ VIRTUAL\033[m')
print('\033[1:36m-=-\033[m' * 20)
print('Olá meu caro, eu te desafio a um jogo de Jokenpô\n'
      'Se você ganhar, te dou meus parabéns\n'
      'Se eu ganhar ou empatar, jogue novamente!')
vc = int(input('Vamos lá: Pedra (0), Papel (1) ou Tesoura (2)? '))
pc = randint(0, 2)
itens = ['\033[37mPEDRA\033[m', 'PAPEL', '\033[31mTESOURA\033[m']
print('\033[1:36m-=-\033[m' * 10)
print('\033[32mJO\033[m')
sleep(0.5)
print('\033[35mKEN\033[m')
sleep(0.5)
print('\033[31mPÔ!\033[m')
sleep(0.3)
print('\033[1:36m-=-\033[m' * 10)
print('Você escolheu {}\n'
      'Eu escolhi {}'.format(itens[vc], itens[pc]))
if (vc == 0 and pc == 0) or (vc == 1 and pc == 1) or (vc == 2 and pc == 2):
    print('Empatamos!')
elif (vc == 0 and pc == 1) or (vc == 1 and pc == 2) or (vc == 2 and pc == 0):
    print('Eu ganhei!')
elif (vc == 0 and pc == 2) or (vc == 1 and pc == 0) or (vc == 2 and pc == 1):
    print('Parabéns! Você ganhou de mim')
