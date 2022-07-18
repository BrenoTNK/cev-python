print('============== Lojas Top ==============')
preco = float(input('Digite o preço das compras R$'))
print('Formas de pagamentos:')
print('1 - à vista dinheiro/cheque')
print('2 - à vista cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')
forma = int(input('Digite o número da forma de pagamento: '))

print('-=-' * 22)
if forma == 1:
    valor = preco * 0.9
    print('A sua compra à vista em dinheiro/cheque tem 10% de desconto.')
    print(f'O valor de R${preco:.2f} vai custar R${valor:.2f} no final.')
elif forma == 2:
    valor = preco * 0.95
    print('A sua compra à vista no cartão tem 5% de desconto.')
    print(f'O valor de R${preco:.2f} vai custar R${valor:.2f} no final.')
elif forma == 3:
    print('A sua compra em 2x no cartão o valor da compra é R${:.2f}.')
    print(f'As parcelas serão de R${preco / 2:.2f} no final.')
elif forma == 4:
    valor = preco * 1.2
    parcela = int(input('Quantas parcelas deseja dividir: '))
    print('-=-' * 22)
    print(f'A compra no cartão em {parcela}x vem com 20% de juros.')
    print(f'O valor de R${preco:.2f} vai para R${valor:.2f} com parcelas de R${valor / parcela:.2f}')
else:
    print('Você digitou um valor inválido! Tente novamente!')
print('-=-' * 22)
