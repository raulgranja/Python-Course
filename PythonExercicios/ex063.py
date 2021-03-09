n = int(input('Digite um número inteiro: '))
n0 = contador = 0
n1 = 1
print('{} {}'.format(n0, n1), end=' ')
while contador < (n - 2):
    n2 = n0 + n1
    print(n2, end=' ')
    n0 = n1
    n1 = n2
    contador += 1
