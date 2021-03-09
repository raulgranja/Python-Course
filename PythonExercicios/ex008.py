print('==== Conversor de metros para centímetros e milímetros ====')

m = int(input('Insira a quantidade em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print('{} metros em milímetros é {}'.format(m, mm))
print(f'{m} metros em centímetros é {cm}')
print(f'{m} metros em decímetros é {dm}')
print(f'{m} metros em decâmetros é {dam}')
print(f'{m} metros em hectômetros é {hm}')
print(f'{m} metros em quilômetros é {km}')
