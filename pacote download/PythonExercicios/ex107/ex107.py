import moeda
n = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {n} é R$ {moeda.metade(n):.2f}')
print(f'O dobro de R$ {n} é R$ {moeda.dobro(n):.2f}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(n, 10):.2f}')
print(f'Diminuindo 10% temos R$ {moeda.diminuir(n, 10):.2f}')
