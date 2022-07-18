# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz = [[], [], []]       #

for i in range(0, 3):
    for c in range(0, 3):
        # matriz[i][c] = int(input(f'Digite um valor para [{i}, {c}]: '))
        matriz[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))      #

print('-='* 20)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end = '')
    print()
print('-='* 20)
