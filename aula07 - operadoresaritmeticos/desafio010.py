cotacao = 3.27    # "Dias de luta, dias de glória"
real = float(input('Digite quanto de dinheiro você tem R$'))

dolares = real / cotacao

print('Com R${} você consegue comprar US${:.2f}.'.format(real, dolares))
