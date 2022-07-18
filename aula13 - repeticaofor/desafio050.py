soma = 0
count = 0
for i in range(0, 6):
    n = int(input(f'Digite o {i + 1}° número: '))
    if n % 2 == 0:
        soma += n
        count += 1
print('-=' * 25)
print(f'A soma entre os {count} números pares digitados é {soma}.')
print('-=' * 25)
