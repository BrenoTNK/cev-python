# matriz = [[], [], []]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]      #
soma_pares = soma_coluna3 = maior_linha2 = 0

for i in range(0, 3):
    for c in range(0, 3):
        # matriz[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))
        matriz[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))     #

        if matriz[i][c] % 2 == 0:
            soma_pares += matriz[i][c]
        if c == 2:
            soma_coluna3 += matriz[i][c]
        if matriz[1][c] > maior_linha2:     #
            maior_linha2 = matriz[1][c]     #
        # if i == 1 and c == 0:
        #     maior_linha2 = matriz[i][c]
        # elif i == 1:
        #     if matriz[i][c] > maior_linha2:
        #         maior_linha2 = matriz[i][c]

print('-='* 25)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end = '')
    print('')
print('-='* 25)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')
print(f'O maior valor da segunda linha é {maior_linha2}')
