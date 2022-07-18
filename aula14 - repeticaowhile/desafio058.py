from random import randint
computador = randint(0, 10)
tentativa = 0

print('Tente adivinhar o número que a máquina pensou.')
jogador = int(input('Digite um número entre 0 e 10: '))
while jogador != computador:
    tentativa += 1

    print('-=' * 25)
    print('Você errou! Tente novamente!')
    print('Dica: É maior.' if computador > jogador else 'Dica: É menor.')
    print('-=' * 25)
    jogador = int(input('Digite um número entre 0 e 10: '))

print('-=' * 25)
print('Parabéns!!!')
print(f'Você acertou! Você precisou de {tentativa} tentativas.')
print('-=' * 25)
