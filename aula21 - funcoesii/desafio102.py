def fatorial(n, show=False):
    """
    -> Calcular o Fatorial de um número
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o calculo.
    :return: O valor do Fatorial de um número n.
    """            
    f = 1
    for c in range(n, 0, -1):
        # Calculo do Fatorial de 'n'.
        f *= c
        if show:
            # Mostrar a conta.
            print(f'{c} ', end='')
            if c > 1:
                print('x ', end='')
            else:
                print('x ', end='')
    return f


print(fatorial(5, True))
