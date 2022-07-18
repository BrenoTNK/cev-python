soma = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        count += 1
print('-=' * 36)
print(f'A soma dos {count} números ímpares entre 1 e 500 multiplos de três é {soma}.')
print('-=' * 36)