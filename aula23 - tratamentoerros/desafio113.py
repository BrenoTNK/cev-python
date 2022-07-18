def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[4;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[4;31mUsuário interrompeu o programa!\033[m')
            return 0
        else:
            return valor


def leiaReal(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('\033[4;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[4;31mUsuário interrompeu o programa!\033[m')
            return 0
        else:
            return valor


# Programa Principal
inteiro = leiaInt('Digite um Inteiro: ')
real = leiaReal('Digite um Real: ')
print(f'O número inteiro digitado foi {inteiro} e o real foi {real}')
