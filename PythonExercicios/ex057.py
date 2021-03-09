genero = str(input('Digite seu gênero [M/F]: ')).strip().upper()[0]
while genero not in 'FM':
    genero = str(input('Gênero inválido, tente novamente [M/F]: ')).strip().upper()[0]
print('Gênero registrado ({})'.format(genero))
