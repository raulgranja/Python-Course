lista = list()
for i in range(5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for elem in range(len(lista)):
            if valor <= lista[elem]:
                lista.insert(elem, valor)
                print(f'Adicionado na posição {elem} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
