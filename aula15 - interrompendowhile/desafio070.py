p_barato = mais = total = 0

while True:
    print('-=' * 20)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto R$'))

    com = ' '
    total += preco
    if preco > 1000:
        mais += 1
    if preco < p_barato or total == preco:
        p_barato = preco
        n_barato = nome

    while com not in 'SsNn':
        com = str(input('Quer continuar? [S/N]: ')).strip()[0]
    if com in 'Nn':
        break

print('-=' * 25)
print(f'''
O total da compra foi de R${total:.2f}.
Há {mais:.2f} produtos com valor maior que R$1000.00
O produto mais barato se chama {n_barato.capitalize()}
''')
print('-=' * 25)
