def area(l, c):
    print(f'A área de um terreno {l} x {c} é de {l * c:.2f} m².')


# main
print('Controle de Terrenos')
print('--------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
