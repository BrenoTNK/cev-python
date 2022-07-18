vel = int(input('Digite a velocidade em km/h do veiculo: '))

print('-=-' * 15)
if vel > 80:
    multa = (vel - 80) * 7.0
    print('Você foi multado por exceder 80km/h!')
    print(f'Sua multa será de R${multa}!')
else:
    print('Você está no limite de velocidade.')
print('-=-' * 15)
