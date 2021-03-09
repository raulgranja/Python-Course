dicionario = dict()
dicionario['nome'] = str(input('Nome: ')).capitalize()
dicionario['média'] = float(input(f'Média de {dicionario["nome"]} '))
print('-=' * 30)
if dicionario['média'] < 7.0:
    dicionario['situação'] = 'Reprovado'
else:
    dicionario['situação'] = 'Aprovado'
for k, v in dicionario.items():
    print(f'  - {k} é igual a {v}')
print(dicionario)
