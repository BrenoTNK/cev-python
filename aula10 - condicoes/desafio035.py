a = float(input('Digite um lado do triângulo: '))
b = float(input('Digite outro lado do triângulo: '))
c = float(input('Digite mais um lado do triângulo: '))

if a < b + c and b < a + c and c < a + b:
    print('É possivel fazer um triângulo com esses valores!')
else:
    print('NÃO é possivel fazer um triângulo com esses valores!')
