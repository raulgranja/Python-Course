dados = dict()
dados['nome'] = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
gols = list()
# soma = 0
for i in range(partidas):
    g = int(input(f'   Quantos gols na partida {i + 1}? '))
    gols.append(g)
    # soma += g
dados['gols'] = gols[:]
# dados['total'] = soma
dados['total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for i, g in enumerate(gols):
    print(f'   => Na partida {i + 1}, fez {g} gols.')
print(f'Foi um total de {dados["total"]} gols.')
