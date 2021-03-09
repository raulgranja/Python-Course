print('\033[1:33mCALCULADORA DE IMC\033[m')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC = \033[33m{:.2f}\033[m\n'
          'Você está \033[32mabaixo do peso\033[m'.format(imc))
elif 18 <= imc < 25:
    print('IMC = \033[1:32m{:.2f}\033[m\n'
          'Você está no \033[1:32mpeso ideal\033[m'.format(imc))
elif 25 <= imc < 30:
    print('IMC = \033[1:33m{:.2f}\033[m\n'
          'Você está com \033[1:33msobrepeso\033[m'.format(imc))
elif 30 <= imc < 40:
    print('IMC = \033[31m{:.2f}\033[m\n'
          'Você está com \033[31mobesidade\033[m'.format(imc))
else:
    print('IMC = \033[1:31m{:.2f}\033[m\n'
          'Você está com \033[1:31mobesidade mórbida\033[m'.format(imc))
