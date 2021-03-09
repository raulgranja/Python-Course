print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
saque = int(input('Qual valor você quer sacar? R$ '))
while True:
    cedulas = saque // 50
    if cedulas != 0:
        print(f'Total de {cedulas} cédulas de R$ 50')
    saque -= cedulas * 50
    cedulas = saque // 20
    if cedulas != 0:
        print(f'Total de {cedulas} cédulas de R$ 20')
    saque -= cedulas * 20
    cedulas = saque // 10
    if cedulas != 0:
        print(f'Total de {cedulas} cédulas de R$ 10')
    saque -= cedulas * 10
    cedulas = saque // 1
    if cedulas != 0:
        print(f'Total de {cedulas} cédulas de R$ 1')
    saque -= cedulas * 1
    if saque == 0:
        break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
