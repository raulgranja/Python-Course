salario = float(input('Quanto é o seu salário? R$ '))
if salario > 1250:
    print(f'Você terá um aumento de 10%, portanto seu novo salário será R$ {salario * 1.1:.2f}')
else:
    print(f'Você terá um aumento de 15%, portanto seu novo salário será R$ {salario * 1.15:.2f}')
