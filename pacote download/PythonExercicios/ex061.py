n = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
termo = 1
print(n, end=' ')
while termo < 10:
    n += r
    termo += 1
    print(n, end=' ')
