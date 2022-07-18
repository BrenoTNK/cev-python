'''

    As cores não funciona muito bem no terminal do VSCode;

'''

from time import sleep
c = (
    '\033[m',           # 0 - Sem cor;
    '\033[0;30;41m',    # 1 - Vermelho;
    '\033[0;30;42m',    # 2 - verde;
    '\033[0;30;43m',    # 3 - amarelo;
    '\033[0;30;44m',    # 4 - azul;
    '\033[0;30;45m',    # 5 - roxo;
    '\033[7;30m'        # 6 - branco;
)


def pyHelp(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(c[3], end='')
    help(comando)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = (len(msg) + 4)
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    cmd = str(input('Função ou biblioteca > ')).strip().lower()

    if cmd == 'fim': break

    pyHelp(cmd)
titulo('ATÉ LOGO!', 1)
