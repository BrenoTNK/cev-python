a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

    # Verificar o menor número;
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

    # Verificar o maior número;
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor número é: {menor}\nO maior número é: {maior}')
