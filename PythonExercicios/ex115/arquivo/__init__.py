from ex115.menu import cabecalho, leiaint, vermelho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def escrevaArquivo(nome):
    cabecalho('NOVO CADASTRO')
    a = open(nome, 'at')
    try:
        name = str(input('Nome: '))
        idade = str(leiaint("Idade: "))
        a.write(f'{name};{idade}\n')
        return idade
    except:
        print(vermelho('Erro ao inserir os dados.'))
    finally:
        a.close()


def leiaArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            lista = linha.split(';')
            lista[1] = lista[1].replace('\n', '')
            print(f'{lista[0]:<32}{lista[1]} anos')
    finally:
        a.close()

