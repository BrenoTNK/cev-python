from datetime import date

pessoa = {}

pessoa['Nome'] = str(input('Nome: ')).capitalize()
ano_nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = date.today().year - ano_nasc
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))

    aposenta = (pessoa['Contratação'] + 35) - ano_nasc
    pessoa['Aposentadoria'] = aposenta

print('-=' * 20)
for k, v in pessoa.items():
    print(f'    - {k} tem o valor {v}.')
print('-=' * 20)
