from datetime import date
print('\033[34m========== '
      '\033[36mCONFEDERAÇÃO NACIONAL DE NATAÇÃO'
      '\033[34m ==========\033[m')
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Você tem {} anos e está na categoria '
          '\033[35mMIRIM\033[m'.format(idade))
elif 9 < idade <= 14:
    print('Você tem {} anos e está na categoria '
          '\033[34mINFANTIL\033[m'.format(idade))
elif 14 < idade <= 19:
    print('Você tem {} anos e está na categoria '
          '\033[33mJUNIOR\033[m'.format(idade))
elif 19 < idade <= 25:
    print('Você tem {} anos e está na categoria '
          '\033[32mSÊNIOR\033[m'.format(idade))
else:
    print('Você tem {} anos e está na categoria '
          '\033[31mMASTER\033[m'.format(idade))
