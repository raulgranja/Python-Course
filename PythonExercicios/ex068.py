from random import randint
cont = 0
while True:
    jogador = int(input('Digite um valor (De 0 a 10): '))
    paridade = str(input('Par ou Impar? [P/I]: '))
    pc = randint(0, 10)
    print('-=' * 20)
    print(f'Eu escolhi {pc} e a soma foi {jogador + pc}.', end=' ')
    if (jogador + pc) % 2 == 0:
        if paridade in 'pP':
            print('Deu PAR, você ganhou! Jogue novamente')
            print('-=' * 20)
            cont += 1
        elif paridade in 'iI':
            print('Deu PAR, você perdeu...')
            print('GAME OVER')
            break
    elif (jogador + pc) % 2 == 1:
        if paridade in 'iI':
            print('Deu ÍMPAR, você ganhou! Jogue novamente')
            print('-=' * 20)
            cont += 1
        elif paridade in 'pP':
            print('Deu ÍMPAR, você perdeu...')
            print('GAME OVER')
            break
print(f'Você ganhou {cont} vezes seguidas')
