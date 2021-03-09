from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    print('''===== MENU =====
[1] SOMAR
[2] MULTIPLICAR
[3] DIVIDIR
[4] DIGITAR NOVOS NÚMEROS
[5] SAIR''')
    menu = int(input('Digite o número que deseja: '))
    if menu == 1:
        print('Números digitados {} e {}'.format(n1, n2))
        print('\033[31mSoma\033[m: {}'.format(n1 + n2))
        sleep(0.4)
    elif menu == 2:
        print('Números digitados {} e {}'.format(n1, n2))
        print('\033[32mMultiplicação\033[m: {}'.format(n1 * n2))
        sleep(0.4)
    elif menu == 3:
        print('Números digitados: {} e {}'.format(n1, n2))
        print('\033[33mDivisão\033[m: {}'.format(n1 / n2))
        sleep(0.4)
    elif menu == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        sleep(0.2)
    elif menu == 5:
        sleep(0.1)
    else:
        print('Função inexistente, tente novamente')
        sleep(0.5)
print('FIM')
