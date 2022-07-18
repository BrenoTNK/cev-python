from datetime import date

ano = int(input('Digite o seu ano de nascimento: '))

idade = date.today().year - ano

print('-=-' * 15)
if idade < 17:
    print('Ainda não está na hora de se alistar.')
    print(f'Você se alistará daqui a {18 - idade} anos.')
    print(f'Ano de alistamento será {date.today().year + (18 - idade)}.')
elif idade > 18:
    print('Já passou do tempo para se alistar.')
    print(f'Você deveria ter se alistado ha {idade - 18} anos.')
    print(f'Ano de alistamento foi em {date.today().year - (idade - 18)}')
else:
    print('Você tem que se alistar, você já tem 18 anos!')
print('-=-' * 15)
