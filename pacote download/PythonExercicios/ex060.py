n = int(input('Digite um número inteiro: '))
x = n - 1
resultado = 1
if n == 1 or n == 0:
    print('{}! é igual à 1'.format(n))
elif n < 0:
    print('Não existe fatorial para números negativos')
else:
    print('{}! é igual a:'.format(n))
    print(('{}'.format(n)), end='')
    while x >= 1:
        resultado = n * x
        x -= 1
        n = resultado
        print((' x {}'.format(x + 1)), end='')
    print(' = {}'.format(resultado))
