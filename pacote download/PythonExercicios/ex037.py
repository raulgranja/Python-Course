green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
stop = '\033[m'
print('=============== Conversor de Bases Numéricas ===============')

dec = int(input('Digite um número inteiro: '))
conv = int(input('''Para qual base numérica deseja converter?
Digite 1 para sistema {}Binário{}
Digite 2 para sistema {}Octal{}
Digite 3 para sistema {}Hexadecimal{}
'''.format(red, stop, green, stop, yellow, stop)))
b = bin(dec)
o = oct(dec)
h = hex(dec)

if conv == 1:
    print('O número {} em {}Binário{} corresponde a: {}'
          .format(dec, red, stop, b[2:]))
elif conv == 2:
    print('O número {} em {}Octal{} corresponde a: {}'
          .format(dec, green, stop, o[2:]))
elif conv == 3:
    print('O número {} em {}Hexadecimal{} corresponde a: {}'
          .format(dec, yellow, stop, h[2:]))
