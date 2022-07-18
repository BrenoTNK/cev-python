from datetime import date

ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year     # Ele coloca o ano atual do computador;

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'o ano de {ano} NÃO é bissexto!')
