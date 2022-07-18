n = int(input('Digite a quantidade de valores da sequência: '))

i = 0
o = 1
print('-=' * 40)
while n > 0:
    print(f'{i} - ', end = '')
    o += i
    i = o - i
    n -= 1
print('FIM!')
print('-=' * 40)
