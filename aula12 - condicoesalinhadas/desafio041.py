from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year - ano

print('-=-' * 12)
print(f'O atleta tem {idade} anos de idade.')
if idade <= 9:
    print('O atleta está na categoria MIRIM.')
elif idade <= 14:
    print('O atleta está na categoria INFANTIL.')
elif idade <= 19:
    print('O atleta está na categoria JUNIOR.')
elif idade <= 25:
    print('O atleta está na categoria SÊNIOR.')
else:
    print('O atleta está na categoria MASTER.')
print('-=-' * 12)
