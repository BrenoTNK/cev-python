sexo = str(input('Digite o seu sexo: [M/F] ')).strip()[0]
while sexo not in 'MmFf':
    print('Você digitou um valor inválido! Tente novamente!')
    sexo = str(input('Digite o seu sexo: [M/F] ')).strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
