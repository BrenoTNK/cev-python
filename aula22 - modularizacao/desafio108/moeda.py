def moeda(valor = 0, cel = 'R$'):
    # Formatação para valor monetario, por padrão é em reais
    return str(f'{cel}{valor:.2f}').replace('.', ',')


def metade(valor):
    return valor / 2


def dobro(valor):
    return valor * 2


def aumentar(valor, pcen=0):
    return valor * (1 + (pcen / 100))


def diminuir(valor, pcen=0):
    return valor * (1 - (pcen / 100))

