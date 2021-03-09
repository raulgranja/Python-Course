while True:
    num = int(input('Digite um valor para ver sua tabuada (Número negativo para sair): '))
    print('-'*20)
    if num < 0:
        break
    cont = 1
    while cont <= 10:
        print(f'{num}  X {cont:2} = {num * cont}')
        cont += 1
    print('-'*20)
print('[ FINALIZADO ]')
