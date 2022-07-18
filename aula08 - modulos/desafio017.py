from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjasente: '))

#   hi = ((co ** 2) + (ca ** 2)) ** (1 / 2)
#   hi = sqrt((co ** 2) + (ca ** 2))
hi = hypot(co, ca)

print('O triângulo retângulo com catetos {} e {} tem como hipotenusa igual {}.'.format(co, ca, hi))
