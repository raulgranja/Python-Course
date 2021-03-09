def moeda(valor=0, moeda=''):
    return f'{moeda} {valor:.2f}'.replace('.', ',')


def aumentar(preco, fator, moeda=''):
    """
    --> Aumenta em uma dada porcentagem o valor inserido.
    :param preco: valor a ser aumentado
    :param fator: fator de aumento, em porcentagem
    :param moeda: qual a moeda a ser exibida
    :return: valor aumentado
    """
    final = (preco * (1 + fator / 100))
    if moeda == '':
        return f'{final}'.replace('.', ',')
    else:
        return f'{moeda} {final:.2f}'.replace('.', ',')


def diminuir(preco, fator, moeda=''):
    """
    --> Diminui em uma dada porcentagem o valor inserido.
    :param preco: valor a ser diminuído
    :param fator: fator de diminuição, em porcentagem
    :param moeda: qual a moeda a ser exibida
    :return: valor diminuído
    """
    final = (preco * (1 - fator/100))
    if moeda == '':
        return f'{final}'.replace('.', ',')
    else:
        return f'{moeda} {final:.2f}'.replace('.', ',')


def dobro(preco, moeda=''):
    """
    --> Multiplica o valor inserido por 2.
    :param preco: valor a ser multiplicado
    :param moeda: qual a moeda a ser exibida
    :return: valor dobrado
    """
    final = preco * 2
    if moeda == '':
        return f'{final}'.replace('.', ',')
    else:
        return f'{moeda} {final:.2f}'.replace('.', ',')


def metade(preco, moeda=''):
    """
    --> Divide o valor inserido por 2.
    :param preco: valor a ser dividido
    :param moeda: qual a moeda a ser exibida
    :return: metade do valor
    """
    final = preco / 2
    if moeda == '':
        return f'{final}'.replace('.', ',')
    else:
        return f'{moeda} {final:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=10, reducao=5, moeda=''):
    def linha():
        print('-' * 30)
    linha()
    print('RESUMO DO VALOR'.center(30))
    linha()
    print(f'Preço analisado: \tR$ {preco:.2f}'.replace('.', ','))
    print(f'Dobro do preço: \t{dobro(preco, "R$")}')
    print(f'Metade do preço: \t{metade(preco, "R$")}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, "R$")}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, "R$")}')
    linha()
