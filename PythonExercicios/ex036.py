casa = int(input('Digite o valor da casa: R$ '))
salario = int(input('Digite o valor do seu salário: R$ '))
anos = int(input('Em quantos anos você quer pagar? '))
prestacao = casa / (anos * 12)

print('A prestação mensal é de R$ {:.2f}'.format(prestacao))
if prestacao > 0.3 * salario:
    print('O empréstimo solicitado foi \033[31mNEGADO\033[m')
else:
    print('O empréstimo solicitado foi \033[32mAPROVADO\033[m')
