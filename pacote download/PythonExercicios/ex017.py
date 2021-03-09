from math import hypot

a = float(input('Coloque o valor de um cateto: '))
b = float(input('Coloque o valor do outro cateto: '))

print(f'A hipotenusa deste triângulo retângulo tem o valor aproximado de {(hypot(a,b)):.2f}')
