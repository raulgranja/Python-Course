# Esse programa retorna o valor True se a cidade começa com 'Santo'.
cidade = str(input('Em qual cidade você nasceu? ')).strip().lower().split()
primeira = cidade[0]
print('santo' in primeira)
