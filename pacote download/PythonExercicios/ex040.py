n1 = float(input('Nota da P1: '))
n2 = float(input('Nota da P2: '))
media = (n1 + n2) / 2

if media < 5:
    print('Sua média ficou {}, '
          'portanto você foi \033[1:31mREPROVADO\033[m'.format(media))
elif 5 <= media < 7:
    print('Sua média ficou {}, '
          'portanto você está de \033[1:33mRECUPERAÇÃO\033[m'.format(media))
else:
    print('Sua média ficou {}, '
          'parabéns, você foi \033[1:32mAPROVADO\033[m'.format(media))
