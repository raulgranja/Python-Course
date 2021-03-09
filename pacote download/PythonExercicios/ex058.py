from random import choice
listaNumerica = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(choice(listaNumerica))
tentativas = 0
print('Te desafio a adivinhar o número que estou pensando.')
palpite = int(input('Digite um número inteiro de 0 a 10: '))
while palpite != num:
    if 0 <= palpite <= 10:
        palpite = int(input('Você errou, tente novamente: '))
        tentativas += 1
    else:
        palpite = int(input('Qual sua dificuldade em entender que é entre 0 e 10? Tente novamente: '))
        tentativas += 1
print('Você acertou após {} tentativas, eu pensei no número {}'.format(tentativas, num))
