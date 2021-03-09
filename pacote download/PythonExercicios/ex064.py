n = int(input('Digite um número inteiro (999 para sair): '))
soma = contador = 0
while n != 999:
    soma += n
    n = int(input('Digite um número inteiro (999 para sair): '))
    contador += 1
print('A soma entre os todos os {} números digitados foi {}'.format(contador, soma))
