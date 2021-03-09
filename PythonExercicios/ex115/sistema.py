from menu import *
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    lista = ['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema']
    resposta = menu(lista) + 1
    if resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    elif resposta == 1:
        leiaArquivo(arq)
    elif resposta == 2:
        escrevaArquivo(arq)
