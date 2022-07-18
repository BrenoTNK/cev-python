lista = []
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição{i}: ')))

print('-=' * 30)
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor da lista é {max(lista)} nas posições ', end = '')
for count, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{count}... ', end = '')
print(f'\nO menor valor da lista é {min(lista)} nas posições ', end = '')
for count, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{count}... ', end = '')


    ######## Solução com for -- sem o max() e min() -- ########
'''
lista = []
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição{i}: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print('-=' * 30)
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor da lista é {maior} nas posições ', end = '')
for count, valor in enumerate(lista):
    if valor == maior:
        print(f'{count}... ', end = '')
print(f'\nO menor valor da lista é {menor} nas posições ', end = '')
for count, valor in enumerate(lista):
    if valor == menor:
        print(f'{count}... ', end = '')
'''