n = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(n, n + (r * 10), r):
    print(c, end=' ')
