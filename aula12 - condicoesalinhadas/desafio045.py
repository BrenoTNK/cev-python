from random import choice
from time import sleep

lista = ['pedra', 'papel', 'tesoura']

jogador = str(input('Escolha pedra, papel ou tesoura: ')).strip()
jogador = jogador.lower()
computador = choice(lista)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-' * 8)
print(f'Jogador: {jogador.capitalize()}')
print(f'Computador: {computador}')
print('-=-' * 8)
if jogador == 'pedra':
    if computador == 'papel':
        print('Você PERDEU!!')
    elif computador == 'tesoura':
        print('Você GANHOU!!')
    else:
        print('EMPATE!!!')
elif jogador == 'papel':
    if computador == 'tesoura':
        print('Você PERDEU!!')
    elif computador == 'pedra':
        print('Você GANHOU!!')
    else:
        print('EMPATE!!!')
elif jogador == 'tesoura':
    if computador == 'pedra':
        print('Você PERDEU!!')
    elif computador == 'papel':
        print('Você GANHOU!!')
    else:
        print('EMPATE!!!')
else:
    print('Você digitou errado! Tente novamente.')
print('-=-' * 8)
