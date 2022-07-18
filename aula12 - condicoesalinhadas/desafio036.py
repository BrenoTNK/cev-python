print('Aprovação de emprestimo bancário.')
print('-=-' * 15)

casa = float(input('Digite o valor da casa R$'))
salario = float(input('Digite o seu salário R$'))
anos = int(input('Em quantos anos você vai pagar a casa: '))

parcela = casa / (anos * 12)

print('-=-' * 20)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos... \nA prestação será de R${parcela:.2f}')
if parcela > salario * 0.3:
    print('Infelizmente você não pode financear essa casa. =(')
else:
    print('Seu emprestimo foi aprovado!')
print('-=-' * 20)
