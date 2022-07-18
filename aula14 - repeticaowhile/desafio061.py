n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

i = 0
while i < 10:
    print(f'{n}', end = ' -> ')
    n += r
    i += 1
print('Acabou!')
