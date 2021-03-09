from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p = -p
    elif p == 0:
        p = 1
    if i < f:
        for n in range(i, f + 1, p):
            print(n, end=' ')
            sleep(0.3)
        print('FIM!')
    elif i > f:
        for n in range(i, f - 1, -p):
            print(n, end=' ')
            sleep(0.3)
        print('FIM!')


# main
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
