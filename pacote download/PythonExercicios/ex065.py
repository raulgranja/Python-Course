n = int(input('Digite um número inteiro: '))
maior = menor = n
contador = 1
continuar = str(input('Deseja continuar? (S/N): '))
while continuar in 'Ss':
    n1 = int(input('Digite um número inteiro: '))
    n += n1
    contador += 1
    continuar = str(input('Deseja continuar? (S/N): '))
    if n1 > maior:
        maior = n1
    elif n1 < menor:
        menor = n1
if continuar in 'nN':
    print('A média entre todos os valores foi {}'.format(n / contador))
    print('O menor valor digitado foi {}'.format(menor))
    print('O maior valor digitado foi {}'.format(maior))
