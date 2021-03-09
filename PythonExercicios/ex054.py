from datetime import date
ano = date.today().year
maiores = 0
for c in range(1, 8):
    idade = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - idade >= 21:
        maiores += 1
print('Nessa lista tem {} maiores de idade'.format(maiores))
