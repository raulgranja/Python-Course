frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso += frase[c]
if frase == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
