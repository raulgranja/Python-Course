print('====== CONVERSOR DE TEMPERATURAS ======')

C = float(input('Digite a temperatura em ºC: '))
F = (C * 9/5) + 32
K = (C + 273.15)

print(f'Celsius (ºC): {C:.1f}ºC\nFahrenheit (ºF): {F:.1f}ºF\nKelvin (K): {K:.1f}K')
