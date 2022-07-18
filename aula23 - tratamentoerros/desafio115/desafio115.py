from lib.interface import *
from lib.arquivo import *
from time import sleep


'''
    Esse programa faz cadastro de varias pessoas
    e guarda elas em um arquivo, então o que já foi
    cadastrado anteriormente continua salvo. Mesmo
    depois de finalizado.
'''

opcoes = ([
    # Nome das opções
    'Ver pessoas cadastradas.',
    'Cadastrar uma nova pessoa.',
    'Sair do programa'
])


arq = 'pessoas.txt'     # Nome do arquivo

if not arquivoExiste(arq):
    # Verifica se o arquivo não existe
    criarArquivo(arq)                   # Cria o arquivo

while True:
    # Menu e as opções do programa
    resposta = menu(opcoes)

    if resposta == 1:
        # opção para mostrar os cadastros
        listar(arq)
    elif resposta == 2:
        # Opção para cadastrar uma nova pessoa
        nome = str(input('Nome: ')).title()
        idade = leiaInt('idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção para sair do programa
        titulo('Saindo do sistema... Até logo!')
        break
    else:
        # Caso seja digitado algo fora das opções
        print(f'{cores[1]}ERRO! Digite uma opção válida!{cores[0]}')
    sleep(1)
