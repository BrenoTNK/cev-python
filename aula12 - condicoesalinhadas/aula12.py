nome = str(input('Digite o seu nome: '))
if nome == 'Breno':
    print('Que nome bonito!')
elif nome in 'Pedro Maria João José Ana':
    print('Seu nome é bem popular!')
else:
    print('Seu nome é legal!')

print('Tenha um bom dia, {}' .format(nome))
