from math import cos, sin, tan, radians

angulo = float(input('Digite um ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo {} tem como \nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}.'.format(angulo, seno, cosseno, tangente))
