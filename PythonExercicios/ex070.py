print('-' * 30)
print('{: ^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
total = caros = cont = menorpreco = 0
continuar = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    total += preco
    if preco > 1000:
        caros += 1
    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        menorproduto = produto
    if continuar == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {caros} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {menorproduto} que custa R$ {menorpreco:.2f}')
