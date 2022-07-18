soma = count = n = 0
n = int(input('Digite um número ["999" para parar]: '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um número ["999" para parar]: '))

print('-=' * 30)
print(f'Foram digitados {count} números. A soma entre eles foi de {soma}.')
print('-=' * 30)
