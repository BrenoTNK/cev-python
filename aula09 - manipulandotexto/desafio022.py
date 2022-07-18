nome = str(input('Digite o seu nome completo: '))

print(f'Seu nome em maiúsculo: {nome.upper()}.')
print(f'Seu nome em minúsculo: {nome.lower()}.')
print('O nome completo tem {} letras.' .format(len(nome) - nome.count(' ')))

pnome = nome.split()
print('O primeiro nome tem {} letras.' .format(len(pnome[0])))
