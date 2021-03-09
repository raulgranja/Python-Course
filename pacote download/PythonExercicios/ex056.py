soma = 0
maior_idade = 0
mulheres_menores = 0
homem_velho = ''
mulheres = 0
for pessoa in range(1, 5):
    print('===== {}ª PESSOA ====='.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Gênero (f/m): ')).strip()
    soma = (soma + idade)
    if sexo == 'f':
        if idade < 20:
            mulheres_menores += 1
            mulheres += 1
    elif sexo == 'm':
        if pessoa == 1:
            maior_idade = idade
            homem_velho = nome.capitalize()
        if idade > maior_idade:
            homem_velho = nome.capitalize()
print('A média das idades é {}'.format(soma / 4))
print('O nome do homem mais velho é {}'.format(homem_velho))
if mulheres == 0:
    print('Não há mulheres nessa lista')
elif mulheres_menores == 0:
    print('Não há mulheres menores nessa lista')
elif mulheres_menores == 1:
    print('{} mulher tem menos de 20 anos'.format(mulheres_menores))
else:
    print('{} mulheres tem menos de 20 anos'.format(mulheres_menores))
