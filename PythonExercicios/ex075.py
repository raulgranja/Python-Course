tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')
# noves = tres = pares = 0
#for i in tupla:
#    if i == 9:
#        noves += 1
#    elif i == 3:
#        tres = tupla.index(i)
#    if i % 2 == 0:
#        pares += 1
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('Você não digitou o valor 3')
print(f'Os valores pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
