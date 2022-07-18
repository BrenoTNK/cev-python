lista = []
while True:
    lista.append(int(input('Digite um número: ')))

    while True:
        cod = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if cod in 'SN': break
    if cod == 'N': break

print('-=' * 30)
print(f'Foram digitados {len(lista)} números ao todo.')
dec = lista[:]
dec.sort(reverse=True)
print(f'Lista decrescente: {dec}')
print('O valor 5 faz parte da lista.' if 5 in lista else 'Não foi encontrado o valor 5 na lista!')

########### Bonûs - Posições dos 5 ###########

print('O 5 se encontra nas posições: ', end = '' if 5 in lista else '')
for count in range(0 , len(lista)):
    if lista[count] == 5:
        print(f'{count}... ', end = '')
