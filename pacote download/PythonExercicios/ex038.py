a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
violet = '\033[1;35m'
stop = '\033[m'

if a > b:
    print('O {}primeiro{} número é maior ({})'.format(violet, stop, a))
elif a < b:
    print('O {}segundo{} número é maior ({})'.format(violet, stop, b))
else:
    print('Os números possuem o mesmo valor')
