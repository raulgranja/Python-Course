L = list()
# M = list()
while True:
    r = 'q'
    n = int(input('Digite um valor: '))
    L.append(n)
    while r not in 'sSnN':
        r = str(input('Quer continuar? [S/N] '))
    if r in 'nN':
        break
# L.sort()
L.sort(reverse=True)
# for i in range(len(L) - 1, -1, -1):
#    M.append(L[i])
print('-=' * 30)
print(f'Você digitou {len(L)} elementos')
print(L)  # print(M)
if 5 in L:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
