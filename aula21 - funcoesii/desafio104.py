def leiaInt(msg):
    """
    -> Verificador de input até válidar um número inteiro.
    :param n: Mensagem para o input.
    :ruturn: Retorna num se for inteiro.
    """
    while True:
        valor = str(input(msg))

        if valor.isnumeric():
            num = int(valor)
            return num
        else:
            print('\033[4;31mERRO! Digite um número inteiro válido.\033[m')

        ########## Com try ##########

        # try:
        #     num = int(valor)
        #     return num
        # except ValueError:
        #     print('\033[4;31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
