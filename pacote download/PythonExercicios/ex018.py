from math import sin, cos, tan, radians
x = float(input('Digite um ângulo qualquer (entre 0º e 360º): '))
print(f'O valor do SENO é {sin(radians(x)):.2f}\nO valor do COSSENO é {cos(radians(x)):.2f}'
      f'\nO valor da TANGENTE é {tan(radians(x)):.2f}')
