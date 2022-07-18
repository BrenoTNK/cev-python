nome = str(input('Digite o seu nome completo: ')).strip()

n = nome.split()

print('O seu primeiro nome é {}' .format(n[0].capitalize()))
print('O seu último nome é {}' .format(n[-1].capitalize()))
