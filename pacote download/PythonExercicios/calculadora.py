# -*- coding: utf-8 -*-
print("                                      ")
print("-----------CALCULADORA v1.0-----------")
print("                                      ")
print("Realiza operações de soma, subtração, divisão, multiplicação e exponencial")
print("Os sinais de cada uma dessas operações são:")
print("                                      ")
print('(+): soma')
print("(-): subtração")
print("(/): divisão")
print("(*): multiplicação")
print("(**): exponencial")
print("                                      ")
print("Como utilizar:")
print("Por exemplo, se eu quero fazer uma soma de 2+2, eu coloco da seguinte forma:")
print("Digite o primeiro número: 2")
print("Qual é o operador? +")
print("Digite o segundo número: 2")
print("O resultado é: 4 <-- O resultado aparecerá aqui")
print("                                      ")
print("                                      ")
print("                                      ")

sair = False

while not sair:
    valor1 = input("Digite o primeiro número: ")
    valor1 = int(valor1)
    operador = input("Qual é o operador? ")
    valor2 = input("Digite o segundo número: ")
    valor2 = int(valor2)

    if operador == "+":
        print("                                      ")
        print("O resultado é: ", (valor1 + valor2))
        print("                                      ")
    if operador == "-":
        print("                                      ")
        print("O resultado é: ", (valor1 - valor2))
        print("                                      ")
    if operador == "*":
        print("                                      ")
        print("O resultado é: ", (valor1 * valor2))
        print("                                      ")
    if operador == "/":
        print("                                      ")
        print("O resultado é: ", (valor1 / valor2))
        print("                                      ")
    if operador == "**":
        print("                                      ")
        print("O resultado é: ", (valor1 ** valor2))
        print("                                      ")

    teste = input("Deseja sair? (s/n): ")
    if teste == "s":
        sair = True
    if teste == "n":
        sair = False
        print("                                      ")
