def area(lar, com):
    area = lar * com
    print(f'A área de um terreno {lar}x{com} é de {area:.1f}m²')


# Programa principal
print(' Tamanho de Terrenos')
print('---------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
