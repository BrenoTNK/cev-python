num = int(input('Digite o número para ver sua tabuada: '))

print('-=' * 8)
for i in range(1, 11):
    print(f'{num} x {i:2} = {num * i}')
print('-=' * 8)
