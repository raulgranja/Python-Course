n = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
termo = mais = 1
print(n, end=' ')
while termo < 10:
    n += r
    termo += 1
    print(n, end=' ')
while mais != 0:
    mais = int(input('\nDeseja mostrar mais quantos termos? (Digite 0 para sair): '))
    ate = mais + termo
    while termo < ate:
        n += r
        termo += 1
        print(n, end=' ')
