def moeda(valor=0, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')


def aumentar(preco, fator, moeda=''):
    """
    --> Aumenta em uma dada porcentagem o valor inserido.
    :param preco: valor a ser aumentado
    :param fator: fator de aumento, em porcentagem
    :return: valor aumentado
    """
    final = (preco * (1 + fator/100))
    return final


def diminuir(preco,fator):
    """
    --> Diminui em uma dada porcentagem o valor inserido.
    :param preco: valor a ser diminuído
    :param fator: fator de diminuição, em porcentagem
    :return: valor diminuído
    """
    final = (preco * (1 - fator/100))
    return final


def dobro(preco):
    """
    --> Multiplica o valor inserido por 2.
    :param preco: valor a ser multiplicado
    :return: valor dobrado
    """
    final = preco * 2
    return final


def metade(preco):
    """
    --> Divide o valor inserido por 2.
    :param preco: valor a ser dividido
    :return: metade do valor
    """
    final = preco / 2
    return final
