n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite outro número qualquer: '))
n3 = float(input('Digite o último número: '))
if n1 > n2 > n3:
    print(f'O maior número é {n1}')
    print(f'O menor número é {n3}')
if n1 > n3 > n2:
    print(f'O maior número é {n1}')
    print(f'O menor número é {n2}')
if n2 > n3 > n1:
    print(f'O maior número é {n2}')
    print(f'O menor número é {n1}')
if n2 > n1 > n3:
    print(f'O maior número é {n2}')
    print(f'O menor número é {n3}')
if n3 > n1 > n2:
    print(f'O maior número é {n3}')
    print(f'O menor número é {n2}')
if n3 > n2 > n1:
    print(f'O maior número é {n3}')
    print(f'O menor número é {n1}')
