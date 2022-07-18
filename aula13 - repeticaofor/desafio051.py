n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = n + (10 - 1) * r

for i in range(n, decimo + r, r):
    print(f'{i}', end = ' -> ')
print('Acabou!')
