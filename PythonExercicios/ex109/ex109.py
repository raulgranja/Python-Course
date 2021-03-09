import moeda
n = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(n, "R$")} é {moeda.metade(n, "R$")}')
print(f'O dobro de {moeda.moeda(n, "R$")} é {moeda.dobro(n, "R$")}')
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10, "R$")}')
print(f'Diminuindo 10% temos {moeda.diminuir(n, 10, "R$")}')
