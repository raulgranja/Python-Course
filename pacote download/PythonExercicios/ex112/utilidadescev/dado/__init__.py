def leiaDinheiro(chamada):
    while True:
        valor = str(input(chamada)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO: "{valor.strip()}" é um preço inválido!\033[m')
        else:
            return float(valor)
