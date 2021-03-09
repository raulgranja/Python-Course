from random import choice
listaNumerica = [0, 1, 2, 3, 4, 5]
num = int(choice(listaNumerica))
print('Te desafio a adivinhar o número que estou pensando.')
palpite = int(input('Digite um número inteiro de 0 a 5: '))
if palpite == num:
    print('Você ganhou! Eu realmente pensei no número {}'.format(num))
else:
    print('Você perdeu :(  O número que eu pensei foi {}'.format(num))
    if 0 <= palpite <= 5:
        print('')
    else:
        print('Qual sua dificuldade em entender que é entre 0 e 5?')
