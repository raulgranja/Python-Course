lista = list()
maior = menor = 0
for i in range(5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = lista[i]
    elif lista[i] >= maior:
        maior = lista[i]
    elif lista[i] <= menor:
        menor = lista[i]
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c, v in enumerate(lista):   # índice c, valor v
    if v == maior:
        print(f'{c}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}... ', end='')
