time = list()
while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))
    jogador['gols'] = gols[:]
    time.append(jogador)
    jogador['total'] = sum(jogador['gols'])
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
    if r in 'N':
        break
print('-=' * 30)
print(time)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 39)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 39)
while True:
    dados = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    if dados >= len(time) or dados < 0:
        print(f'ERRO! Não existe jogador com código {dados}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[dados]["nome"].upper()}: ')
        for j, g in enumerate(time[dados]["gols"]):
            print(f'    No jogo {j + 1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
