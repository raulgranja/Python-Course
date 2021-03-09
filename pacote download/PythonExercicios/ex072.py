tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dexoito', 'dezenove', 'vinte')
resp = ' '
while resp != 'N':
    resp = ' '
    n = int(input('Digite um número entre 0 e 20: '))
    while not 0 <= n <= 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {tupla[n]}')
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print('{:=^30}'.format(' FINALIZADO '))
