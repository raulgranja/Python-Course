maisde18 = 0
homens = 0
mulheres = 0
while True:
    sexo = ' '
    idade = ' '
    continuar = ' '
    print('''---------------------------
    CADASTRE UMA PESSOA    
---------------------------''')
    while sexo not in 'mMfF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: '))
    if sexo in 'mM':
        homens += 1
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maisde18 += 1
    if sexo in 'fF':
        if idade < 20:
            mulheres += 1
    while continuar not in 'sSnN':
        continuar = str(input('Deseja continuar [S/N]? '))
    if continuar in 'nN':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {maisde18}')
print(f'Ao todo temos {homens} homem(ns) cadastrado(s)')
print(f'E temos {mulheres} mulher(es) com menos de 20 anos')
