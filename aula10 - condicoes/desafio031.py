km = int(input('Digite a distância da viagem em km: '))

passagem = km * 0.45 if km > 200 else km * 0.5

print(f'O valor da passagem da viagem de {km}km é R${passagem:.2f}.')
