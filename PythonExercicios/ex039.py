from datetime import date
nasc = int(input('Informe o seu ano de nascimento: '))
red = '\033[1;31m'
green = '\033[1:32m'
blue = '\033[1:34m'
stop = '\033[m'
ano = date.today().year

if ano - nasc < 18:
    print('Você ainda {}deverá se alistar{} futuramente\n'
          'Faltam {} anos'
          .format(blue, stop, 18 - (ano - nasc)))
elif ano - nasc > 18:
    print('Seu alistamento já {}passou do prazo{} há {} ano(s)'
          .format(red, stop, ano - nasc - 18))
else:
    print('Você {}deve{} se alistar esse ano!'.format(green, stop))
