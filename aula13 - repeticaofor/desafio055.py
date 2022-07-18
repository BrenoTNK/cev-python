maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input(f'Digite o peso da {i + 1}° pessoa (Kg): '))
    if peso > maior:
        maior = peso
    if peso < menor or i == 0:
        menor = peso
print('-=' * 20)
print(f'A pessoa com mais peso tem {maior}Kg.')
print(f'A pessoa com menos peso tem {menor}Kg.')
print('-=' * 20)
