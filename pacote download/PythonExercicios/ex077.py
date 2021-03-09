tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for i in tupla:
    print(f'\nNa palavra {i} temos ', end='')
    for j in i:
        if j in 'AEIOU':
            print(j.lower(), end=' ')
