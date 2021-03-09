e = str(input('Digite a expressão: '))
L = list()
for carac in e:
    if carac in '()':
        L.append(carac)
if L[0] == ')' or L.count('(') != L.count(')') or L[-1] == '(':
    print('Sua expressão está errada!')
else:
    print('Sua expressão está válida!')
