M = [list(), list(), list()]
for i in range(len(M)):
    for j in range(len(M)):
        M[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
print('-=' * 30)
for i in range(len(M)):
    for j in range(len(M[i])):
        print(f'[{M[i][j]:^5}]', end='')
    print()
