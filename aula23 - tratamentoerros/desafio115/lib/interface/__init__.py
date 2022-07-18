cores = (
    # Cores no terminal
    '\033[m',       # 0 - Sem cor
    '\033[31m',     # 1 - Vermelho
    '\033[32m',     # 2 - Verde
    '\033[33m',     # 3 - Amarelo
    '\033[34m'      # 4 - Azul
)


def linha(txt=40):
    # Coloca uma linha
    print('-' * txt)


def titulo(txt):
    # Faz um cabeçalho com titulo
    linha()
    print(f'{txt}'.center(40))
    linha()


def leiaInt(msg):
    # Verifica se um valor é inteiro
    while True:
        # Se não for, vai fica pedindo até ser inteiro
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            # Caso valor que não seja inteiro
            print('\033[4;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            # Caso interrompa, retorna o valor 0
            print('\033[4;31mUsuário interrompeu o programa!\033[m')
            return 0
        else:
            # Se tudo der certo, retorna o valor
            return valor


def menu(lista):
    # Menu do programa principal
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        # Coloca o código e o nome da opção no menu
        print(f'{cores[3]}{c}{cores[0]} - {cores[4]}{item}{cores[0]}')
        c += 1
    linha()
    opc = leiaInt(f'{cores[2]}Sua opção: {cores[0]}')   # Só aceita número inteiro
    return opc      # Retorna o valor

