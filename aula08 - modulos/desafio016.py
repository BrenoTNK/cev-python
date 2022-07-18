from math import trunc      # Trunc - "Corta" a parte fracionada;

n = float(input('Digite um número real qualquer: '))

print('O número {} tem como parte inteira {}.'.format(n, trunc(n)))

'''     2° forma:

n = float(input('Digite um número real qualquer: '))

print('O número {} tem como parte inteira {}.'.format(n, int(n)))
'''
