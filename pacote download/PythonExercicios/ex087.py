M = [list(), list(), list()]
for i in range(len(M)):
    for j in range(len(M)):
        M[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
print('=-' * 30)
pares = soma = maior = 0
for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] % 2 == 0:
            pares += M[i][j]
        if j == 2:
            soma += M[i][j]
        if i == 1:
            if j == 0 or M[i][j] > maior:
                maior = M[i][j]
        print(f'[{M[i][j]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
