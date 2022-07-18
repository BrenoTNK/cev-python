from math import sqrt
import random

# ceil  = Arredonda pra cima;
# floor = Arredonda pra baixo;

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}.'.format(num, raiz))


####### Random #######

num = random.randint(1, 10)
print(num)
