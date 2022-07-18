from time import sleep

media = m_menores = 0
i_velho = -1
for i in range(0, 4):
    print(f'-=-=-=- {i + 1}° PESSOA -=-=-=-')
    nome = str(input(f'Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    media += idade      # Somar toda as idades;

    if sexo in 'Mm' and idade > i_velho:
        # Descobrir o nome e a idade do homem mais velho;
        n_velho = nome
        i_velho = idade
    if sexo in 'Ff' and idade < 20:
        # Contar quantas mulher tem menos de 20 anos;
        m_menores += 1

media /= 4

print('-=' * 10)
    # Só para parecer que está sendo analisando...
print('ANALISANDO DADOS...')
sleep(3)
print('CONCLUIDO!!')
sleep(1)

print('-=' * 35)
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho se chama {n_velho.title()} e tem {i_velho} anos de idade.')
print(f'Há no grupo {m_menores} mulheres menores de 20 anos.')
print('-=' * 35)
