lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))

    while True:
        cod = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if cod in 'SN': break
    if cod == 'N': break

for i, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print('-=' * 30)
print(f'A lista completa é: {lista}')
print(f'A lsita de pares é: {par}')
print(f'A lsita de ímpares é: {impar}')
print('-=' * 30)
