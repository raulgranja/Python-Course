l = float(input('Qual a largura da parede que você quer pintar? '))
a = float(input('Qual a altura da parede que você quer pintar? '))
Area = l * a
Litros = Area / 2

print(
    'A área da sua parede é de {}m², sendo assim você precisará de {} litros de tinta para pintà-la totalmente'.format(
        Area, Litros))
