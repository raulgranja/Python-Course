from random import choice
vel = choice((range(50, 90)))
print('Você passou no radar com {} km/h'.format(vel))
if vel > 80:
    acima = vel - 80
    multa = 7 * acima
    print('Portanto, você terá de pagar uma multa no valor de R$ {},00.'.format(multa))
else:
    print('Está dentro do limite de velocidade (80 km/h).')
