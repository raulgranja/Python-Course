from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: ')).capitalize()
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem) '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
