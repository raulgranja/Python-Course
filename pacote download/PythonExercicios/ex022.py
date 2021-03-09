nome = str(input('Digite seu nome completo: ')).strip()
nospace = len(nome.replace(' ', ''))

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {nospace} letras')
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.capitalize().split()[0], len(nome.split()[0])))
