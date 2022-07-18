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


def resumo(valor, aumento=10, reducao=5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-' * 35)
