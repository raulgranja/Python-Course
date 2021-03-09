print('====== ALUGUEL DE CARROS ======')

km = float(input('Quantos Km o carro rodou? '))
dias = int(input('Quantos dias você ficou com o carro? '))
p = 60 * dias + 0.15 * km

print(f'O preço a se pagar pelo carro é R$ {p:.2f}')
