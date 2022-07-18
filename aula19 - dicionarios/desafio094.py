lista = []
pessoa = {}
media = 0

while True:
    # Leitura dos dados;
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF': break
        print('--' * 30)
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))

    media += pessoa['idade']
    lista.append(pessoa.copy())

    while True:
        # Se vai continuar a colocar dados;
        cod = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if cod in 'SN': break
        print('--' * 30)
        print('ERRO! Por favor, digite apenas S ou N.')
    if cod == 'N': break

media /= len(lista)

print('-=' * 30)
    # Mostrar dados
print(f'  - O grupo tem {len(lista)} pessoas.')
print(f'  - A média de idade é de {media:.2f} anos.')
print(f'  - As mulheres cadastradas foram: ', end = '')
for p in lista:
    # Mostrar as mulheres;
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end = ' ')
print()
print(f'  - Lista das pessoas que estão acima da média de idade: \n')
for p in lista:
    # Mostrar as pessoas com idade acima da média;
    if p['idade'] >= media:
        print('    ', end = '')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()
print(f'{"-=-=- PROGRAMA ENCERRADO -=-=-":^60}')
