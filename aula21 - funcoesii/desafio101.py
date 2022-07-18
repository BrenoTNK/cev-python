def voto(ano_nasc):
    """
    -> Verifica a idade da pessoa em relação ao voto;
    :param ano_nasc: Ano de nascimento.
    :return: Se o voto é obrigatorio, opcional ou negado.
    """
    from datetime import date
    atual = date.today().year

    idade = atual - ano_nasc

    if idade <  16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 17 < idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


print('--' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
