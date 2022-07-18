a = float(input('Digite um lado do triângulo: '))
b = float(input('Digite outro lado do triângulo: '))
c = float(input('Digite mais um lado do triângulo: '))

print('-=-' * 18)
if a < b + c and b < a + c and c < a + b:
    print('É possivel fazer um triângulo com esses valores!')
    if a == b == c:     # Que coisa mais linda!!
        print('O triângulo será EQUILÁTERO.')
    elif a != b != c != a:
        print('O triângulo será ESCALENO.')
    else:
        print('O triângulo será ISÓSCELES.')
else:
    print('NÃO é possivel fazer um triângulo com esses valores!')
print('-=-' * 18)