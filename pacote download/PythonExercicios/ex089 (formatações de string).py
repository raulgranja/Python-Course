lista = list()
while True:
    temp = list()
    temp.append(str(input('Nome: ')).capitalize())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lista.append(temp)
    r = 'q'
    while r not in 'sSnN':
        r = str(input('Quer continuar? [S/N] '))
    if r in 'nN':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{(a[1] + a[2]) / 2:>8.1f}')
# Como eu tinha feito as duas linhas acima:
# for i in range(len(lista)):
#     print(f'{i:<3}', end=' ')
#     print(f'{lista[i][0]:<15}', end=' ')
#     print(f'{(lista[i][1] + lista[i][2]) / 2:>5}')
while True:
    print('-' * 35)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    if mostrar <= len(lista) - 1:
        print(f'As notas de {lista[mostrar][0]} são [{lista[mostrar][1]}, {lista[mostrar][2]}]')
print('FINALIZANDO...')
print('<<< Volte sempre! >>>')
