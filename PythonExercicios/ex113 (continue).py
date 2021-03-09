def leiaint(num):
    while True:
        try:
            v = int(input(num))
            break
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return v


def leiafloat(num):
    while True:
        try:
            v = float(input(num))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return v


# main
n = leiaint('Digite um Inteiro: ')
m = leiafloat('Digite um Real: ')
print(f'O valor inteiro foi {n} e o real foi {m}')
