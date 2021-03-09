import urllib.error
import urllib.request
try:
    urllib.request.urlopen("http://pudim.com.br").getcode()
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!')
