########## Com while ##########

valor = int(input('Digite um número para encontrar seu fatorial: '))
i = valor
n = 1

print('-=' * 40)
print(f'Calculando {valor}! = ', end = '')
while i > 0:
    print(f'{i}', end = '')
    print(' x ' if i > 1 else ' = ', end = '')
    n *= i
    i -= 1
print(n)
print('-=' * 40)

########## Com for ##########

'''
valor = int(input('Digite um número para encontrar seu fatorial: '))
n = 1

print('-=' * 40)
print(f'Calculando {valor}! = ', end = '')
for i in range(valor, 0, -1):
    print(f'{i}', end = '')
    print(' x ' if i > 1 else ' = ', end = '')
    n *= i
print(n)
print('-=' * 40)
'''

########## Com a biblioteca math ##########

'''
from math import factorial
valor = int(input('Digite um número para encontrar seu fatorial: '))
f = factorial(valor)

print('-=' * 20)
print(f'O fatorial de {valor} é igual: {f}.')
print('-=' * 20)
'''