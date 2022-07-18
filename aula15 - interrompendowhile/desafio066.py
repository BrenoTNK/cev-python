count = soma  = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))

    if n == 999:
        break

    count += 1
    soma += n

print('-=' * 25)
print(f'Os {count} números digitados tem soma total {soma}.')
print('-=' * 25)
