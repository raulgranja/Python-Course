galera = list()
mai = men = 0
while True:
    pessoa = list()
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    if pessoa[1] > mai:
        mai = pessoa[1]
    if pessoa[1] < men or len(galera) == 1:
        men = pessoa[1]
    r = 'q'
    while r not in 'sSnN':
        r = str(input('Deseja continuar? [S/N] '))
    if r in 'nN':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso foi de {mai} kg. Peso de ', end='')
for i in galera:
    if i[1] == mai:
        print(f'[{i[0]}] ', end='')
print(f'\nO menor peso foi de {men} kg. Peso de ', end='')
for i in galera:
    if i[1] == men:
        print(f'[{i[0]}] ', end='')
