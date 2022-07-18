compras = (
    'Guaraná', 6.25,
    'Feijão', 13.50,
    'Molho de tomate', 3.40,
    'Chocolate', 8.50,
    'Batata', 4.80,
    'Frango', 10.90,
    'Pipoca', 9.40,
    'Arroz', 25.00,
    'Leite', 8.00
)

print('-=' * 20)
print('{:^40}' .format('LISTA DE PREÇOS'))
print('-=' * 20)
for i in range(0, len(compras)):
    if i % 2 == 0:
        print(f'{compras[i]:.<30}', end = '')
    else:
        print(f'R${compras[i]:>8.2f}')
print('-=' * 20)
