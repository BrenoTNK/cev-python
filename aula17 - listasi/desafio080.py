lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um número: ')))
    
    if lista[i] > max(lista) or i == 0:
        print('Adicionado no final da lista...')
    else:
        for count, valor in enumerate(lista):
            if lista[i] <= valor:
                lista.insert(count, lista[i])
                lista.pop()
                print(f'Adicionado na posição {count} da lista...')
                break
print('-=' * 27)
print(f'Os valores digitados em ordem foram: {lista}')
