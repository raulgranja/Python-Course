def leiaint(num):
    while True:
        v = input(num)
        if v.isnumeric():
            v = int(v)
            return v
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# main
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
