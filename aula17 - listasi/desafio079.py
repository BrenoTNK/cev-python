lista = []
while True:
    n = int(input('Digite um número: '))

    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valore repetido, não vou adicionar...')
    
    while True:
        cod = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if cod in 'SN': break
    if cod == 'N': break

lista.sort()
print(f'Você digitou os valores {lista}')
