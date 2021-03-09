s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c  # Isso é igual a s recebe s + c, ou s = s + c
print('O somatório de todos os números ímpares múltiplos de 3 no intervalo de 1 a 500 é {}'.format(s))
