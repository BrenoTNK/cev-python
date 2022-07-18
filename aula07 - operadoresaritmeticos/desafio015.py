dias = int(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos kilometros foram rodados pelo carro: '))

aluguel = (dias * 60) + (km * 0.15)

print('O valor total a ser pago é de R${:.2f}.'.format(aluguel))
