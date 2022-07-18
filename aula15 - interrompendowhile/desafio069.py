maiores = homem = m_mulher = 0

while True:
    print('-=-=-=-=-=-=-= CADASTRE UMA PESSOA =-=-=-=-=-=-=-')
    sexo = com = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip()[0]

    if idade >= 18:
        maiores += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        m_mulher += 1

    while com not in 'SsNn':
        com = str(input('Dejesa continuar? [S/N]: ')).strip()[0]
    if com in 'Nn':
        break

print('-=' * 20)
print(f'''
    Há {maiores} pessoa(s) maiores de 18 anos.
    Ao todo, há {homem} homem(ns) cadastrado(s).
    Há {m_mulher} mulher(es) menor(es) de 20 anos.
''')
print('-=' * 20)
