total_ced = 0
ced = 50

print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                BANCO CEV 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')

valor = int(input('Que valor você quer sacar? R$'))
total = valor
t_ced = 0

while True:
    if total >= ced:
        total -= ced
        t_ced += 1
    else:
        if t_ced > 0:
            print(f'Total de {t_ced} de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        t_ced = 0
        if total == 0:
            break

print(''' -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Volte sempre no BANCO DEV! Tenha um bom dia!
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')


############ Sem while ############


"""
cinquenta = vinte = dez = um = 0

valor = int(input('Que valor você quer sacar? R$'))

if valor >= 50:
    cinquenta = valor // 50
    valor %= 50
    print(f'Total de {cinquenta} cédulas de R$50')
if valor >= 20:
    vinte = valor // 20
    valor %= 20
    print(f'Total de {vinte} cédulas de R$20')
if valor >= 10:
    dez = valor // 10
    valor %= 10
    print(f'Total de {dez} cédulas de R$10')
if valor >= 1:
    um = valor // 1
    valor %= 1
    print(f'Total de {um} cédulas de R$1')

"""