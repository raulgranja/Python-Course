lista = list()
valor = 0
resp = 's'
while resp in 'sS':
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = 'r'
    while resp not in 'sSnN':
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'nN':
            break
lista.sort()
print(f'Você digitou os valores {lista}')
