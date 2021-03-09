times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio',
         'Corinthians', 'Bragantino', 'Santos', 'Athletico-PR', 'Ceará SC', 'Atlético-GO', 'Vasco da Gama',
         'Bahia', 'Sport Recife', 'Fortaleza', 'Goiás', 'Coritiba', 'Botafogo')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O São Paulo está na posição {times.index("São Paulo") + 1}')
print('-=' * 15)
