from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for i in tupla:
    print(f'{i} ', end='')

# ordem = sorted(tupla)
# print(f'\nO maior valor sorteado foi {ordem[-1]}')
# print(f'O menor valor sorteado foi {ordem[0]}')

print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
