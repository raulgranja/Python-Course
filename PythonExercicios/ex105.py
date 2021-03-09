def notas(*valores, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    d = dict()
    d['total'] = len(valores)
    maior = menor = 0
    for i, v in enumerate(valores):
        if i == 0:
            maior = v
            menor = v
        elif v > maior:
            maior = v
        elif v < menor:
            menor = v
    d['maior'] = maior
    d['menor'] = menor
    d['média'] = sum(valores) / len(valores)
    if sit:
        if d['média'] < 5.0:
            d['situação'] = 'RUIM'
        elif 5.0 <= d['média'] < 7.0:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'BOA'
    return d


# main
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
help(notas)
