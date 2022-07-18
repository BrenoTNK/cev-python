maior = menor = count = media = 0
resp = 'S'

while resp in 'Ss':
    n = int(input('Digite um número: '))

    if n > maior or count == 0:
        maior = n
    if n < menor or count == 0:
        menor = n

    media += n
    count += 1
    resp = str(input('Você quer continuar? [S/N]: '))

media /= count

print('-=' * 20)
print(f'A média dos números foi: {media:.2f}.')
print(f'O maior número foi: {maior}\nO menor número foi: {menor}')
print('-=' * 20)
