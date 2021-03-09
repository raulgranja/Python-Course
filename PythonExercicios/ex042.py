a = float(input('Digite o lado "a" do triângulo: '))
b = float(input('Digite o lado "b" do triângulo: '))
c = float(input('Digite o lado "c" do triângulo: '))

if a + b > c and a + c > b and b + c > a:
    print('Esse triângulo existe')
    if a == b == c:
        print('É um triângulo \033[36mequilátero\033[m (todos os lados iguais)')
    elif a == b != c or a == c != b or b == c != a:
        print('É um triângulo \033[36misósceles\033[m (dois lados iguais)')
    else:
        print('É um triângulo \033[36mescaleno\033[m (nenhum lado igual)')
else:
    print('Esse triângulo não existe')
