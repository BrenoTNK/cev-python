n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
i = 0
c = 10

while i < c:
    print(f'{n}', end = ' -> ')
    n += r
    i += 1
    if i == c:
        c += int(input('\nQuantos termos você quer mostrar a mais? '))

print('-=' * 30)
print(f'Finalizado! A progressão possui {i} termos mostrados.')
print('-=' * 30)


########### Forma do video ###########

'''
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

i = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while i < total:
        print(f'{n}', end = ' -> ')
        n += r
        i += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('-=' * 30)
print(f'Finalizado! A progressão possui {total} termos mostrados')
print('-=' * 30)
'''
