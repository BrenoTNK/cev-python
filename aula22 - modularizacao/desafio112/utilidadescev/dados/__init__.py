def leiaDinheiro(txt):
    while True:
        valor = str(input(txt)).strip().replace(',', '.')

        if valor.isalpha() or valor == '':
            print(f'\033[4;31mERRO! "{valor}" é um preço inválido!.\033[m')
        else:
            valor = float(valor)
            return valor

        ########## Com try ##########

        # try:
        #     valor = float(valor)
        #     return valor
        # except ValueError:
        #     print(f'\033[4;31mERRO! "{valor}" é um preço inválido!.\033[m')
