print(f'{" LOJAS RAUL ":=^40}')
preco = float(input('Digite o preço do produto: R$ '))
pagamento = int(input('Qual será a condição de pagamento?\n'
                      '0 para pagamento à vista no boleto\n'
                      '1 para pagamento à vista no cartão\n'
                      'Para pagamento parcelado de 2x até 12x, digite o número de parcelas\n'
                      'Digite: '))

if pagamento == 0:
    print('Temos desconto de 10% para pagamento à vista no boleto, \n'
          'portanto o produto terá o valor de R$ {}'.format(0.9 * preco))
elif pagamento == 1:
    print('Temos desconto de 5% para pagamento à vista no cartão, \n'
          'portanto o produto terá o valor de R$ {}'.format(0.95 * preco))
elif pagamento == 2:
    print('Você realizará o pagamento em 2x de R$ {}'.format(preco / 2))
elif 2 < pagamento <= 12:
    print('Você realizará o pagamento em {}x de R$ {} '
          'com 20% de juros'.format(pagamento, (preco * 1.20) / pagamento))
