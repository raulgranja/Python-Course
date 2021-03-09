def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param n: O número a ser calculado;
    :param show: (opcional) Mostrar ou não a conta;
    :return: O valor do Fatorial de um número n.
    """
    for i in range(n, 1, -1):
        n *= i - 1
        if show:
            print(f'{i} x ', end='')
    if show:
        print(f'1 = ', end='')
    print(n)


# main
fatorial(5, show=True)
help(fatorial)
