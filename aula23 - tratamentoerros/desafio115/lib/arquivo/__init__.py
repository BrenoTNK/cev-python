from lib.interface import *


def arquivoExiste(nome):
    # Verifica se o arquivo .txt existe
    try:
        # Ler o arquivo
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        # Se não achar, retorna que não
        return False
    else:
        # Se achar, retorna que sim
        return True


def criarArquivo(nome):
    # Cria o arquivo .txt para os cadastros
    try:
        # Tenta criar o arquivo
        a = open(nome, 'wt+')
        a.close()
    except:
        # Caso dê algum erro ao criar, mostra:
        print(f'{cores[1]}Houve um ERRO na criação do arquivo!{cores[0]}')
    else:
        # Caso dê certo, mostra:
        print(f'{cores[2]}Arquivo criado com sucesso!{cores[0]}')


def cadastrar(arq, nome='desconhecido', idade=0):
    # Cadastro de pessoas
    titulo('NOVO CADASTRO')
    try:
        # Abre o arquivo
        a = open(arq,'at')
    except:
        # Se não abrir, mostra:
        print(f'{cores[1]}ERRO! Não foi possível abrir o arquivo!{cores[0]}')
    else:
        # Se abrir:
        try:
            # Tenta cadastrar no arquivo
            a.write(f'{nome};{idade}\n')
        except:
            # Se der algum problema ao escrever, mostra:
            print(f'{cores[1]}ERRO! Houve algum problema na escrita dos dados!{cores[0]}')
        else:
            # Se der certo, mostra:
            print(f'{cores[2]}Novo cadastro foi criado com sucesso!{cores[0]}')
            a.close()


def listar(nome):
    # Mostrar todas as pessoas cadastradas
    titulo('PESSOAS CADASTRADAS')
    try:
        # Abre e lê o arquivo
        a = open(nome, 'rt')
    except:
        # Se não conseguir ler, mostra:
        print(f'{cores[1]}ERRO! Ao ler o arquivo!{cores[0]}')
    else:
        # Se conseguir
        for linha in a:
            # Pega cada linha do arquivo
            dado = linha.split(';')                     # Separa o nome da idade
            dado[1] = dado[1].replace('\n', '')         # Subistitui a quebra de linha para não ficar espaçado
            print(f'{dado[0]:<30} {dado[1]:>3} anos')   # Escreve no terminal
    finally:
        # Por fim, fecha o arquivo
        a.close()
