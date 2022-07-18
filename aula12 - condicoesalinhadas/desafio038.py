n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

print('-=-'* 15)
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
print('-=-' * 15)
