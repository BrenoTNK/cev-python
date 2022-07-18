alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))

area = alt * lar
litros = area/2

print('A área da parede é de {} m², então precisará de {} litros de tinta para pinta-la.'.format(area, litros))
