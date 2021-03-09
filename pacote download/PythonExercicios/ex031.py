dist = int(input('Digite a distância da sua viagem (em km): '))
if dist <= 200:
    print(f'O valor da sua passagem será R$ {dist * 0.50:.2f}')
else:
    print(f'O valor da sua passagem será R$ {dist * 0.45:.2f}')
