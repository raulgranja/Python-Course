def leiaint(txt):
    while True:
        try:
            v = int(input(txt))
            break
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return v


def linha(num=40):
    print('-' * num)


def cabecalho(txt, num=40):
    linha(num)
    print(txt.center(num))
    linha(num)


def vermelho(txt):
    texto = f'\033[31m{txt}\033[m'
    return texto


def verde(txt):
    texto = f'\033[32m{txt}\033[m'
    return texto


def amarelo(txt):
    texto = f'\033[33m{txt}\033[m'
    return texto


def azul(txt):
    texto = f'\033[34m{txt}\033[m'
    return texto


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(amarelo(f'{i + 1}'), end=' ')
        print('-', end=' ')
        print(azul(f'{v}'), end=' ')
        print()
    linha(40)
    while True:
        opc = leiaint(f'{verde("Sua opção: ")}') - 1
        if 0 <= opc < len(lista):
            break
        else:
            print(vermelho('ERRO! Digite uma opção válida.'))
    return opc
