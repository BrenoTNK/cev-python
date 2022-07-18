altura = float(input('Digite a sua altura (m): '))
peso = float(input('Digite o seu peso (km): '))

imc = peso / (altura ** 2)

print('-=-' * 11)
print(f'O IMC dessa pessoa é {imc:.2f}.')
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc < 25:
    print('Você está no PESO IDEAL!')
elif imc < 30:
    print('Você está em SOBREPESO!')
elif imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')
print('-=-' * 11)
