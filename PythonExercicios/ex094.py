lista = list()
soma = 0
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa)
    soma += pessoa['idade']
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r not in 'SN':
            print('ERRO! Responda apenas S ou N.')
        else:
            break
    if r in 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {soma / len(lista):5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for i in lista:
    if i['sexo'] in 'F':
        print(f'{i["nome"]} ', end='')
print('\nD) Lista das pessoas que estão acima da média:\n   ', end='')
for i in lista:
    if i['idade'] >= soma / len(lista):
        for k, v in i.items():
            print(f' {k} = {v}; ', end='')
        print()
