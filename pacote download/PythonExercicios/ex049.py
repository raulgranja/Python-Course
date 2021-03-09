print('==== Tabuada ====')
n = int(input('Digite um número inteiro: '))
for c in range(1, 11):
    print('{} X {:2} = {:2}'.format(n, c, n * c))
