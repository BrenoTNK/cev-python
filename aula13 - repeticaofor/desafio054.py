from datetime import date

menor = 0
maior = 0

for i in range(0, 7):
    ano = int(input(f'Digite o ano de nascimento da {i + 1}° pessoa: '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('-=' * 16)
print(f'Quantidade de pessoas menores de idade: {menor}')
print(f'Quantidade de pessoas maiores de idade: {maior}')
print('-=' * 16)
