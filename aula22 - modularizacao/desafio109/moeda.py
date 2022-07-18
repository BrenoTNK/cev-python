def moeda(valor = 0, cel = 'R$'):
    return str(f'{cel}{valor:.2f}').replace('.', ',')


def metade(valor, f=False):
    res = valor / 2
    return res if f is False else moeda(res)


def dobro(valor, f=False):
    res = valor * 2
    return res if f is False else moeda(res)


def aumentar(valor, pcen=0, f=False):
    res = valor * (1 + (pcen / 100))
    return res if f is False else moeda(res)


def diminuir(valor, pcen=0, f=False):
    res = valor * (1 - (pcen / 100))
    return res if f is False else moeda(res)

