a = float(input('Digite o lado "a" de um triângulo: '))
b = float(input('Digite o lado "b" desse triângulo: '))
c = float(input('Digite o lado "c" desse triângulo: '))
if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('Esse triângulo existe')
else:
    print('Não é possível construir um triângulo com essas medidas')
