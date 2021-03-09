frase = str(input('Escreva uma frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.lower().find('a') + 1))
print('A letra A aparece a última vez na posição {}'.format(frase.lower().rfind('a') + 1))
