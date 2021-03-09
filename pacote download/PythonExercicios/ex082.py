L = list()
P = list()
I = list()
while True:
    n = int(input('Digite um número: '))
    L.append(n)
    r = 'q'
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] '))
    if n % 2 == 0:
        P.append(n)
    else:
        I.append(n)
    if r in 'nN':
        break
P.sort()
I.sort()
print('-=' * 30)
print(f'A lista completa é {L}')
print(f'A lista de pares é {P}')
print(f'A lista de ímpares é {I}')
