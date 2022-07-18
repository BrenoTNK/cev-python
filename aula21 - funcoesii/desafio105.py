def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos.
    :param: (Opcional), identificar se deve ou não adicionar a situação.
    :return: Dicionario com várias informações sobre a turma.
    """
    turma = {}
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = (sum(n) / turma['total'])
    if sit:
        # Ver a situação da turma
        if turma['média'] >= 7:
            # Se a média for boa
            turma['situação'] = 'BOA'
        elif turma['média'] >= 5:
            # Se a média for razoável
            turma['situação'] = 'RAZOÁVEL'
        else:
            # Se a média for ruim
            turma['situação'] = 'RUIM'
    return turma


# Programa principal
resp = notas(3, 1, 10, 2, sit=True)
print(resp)
