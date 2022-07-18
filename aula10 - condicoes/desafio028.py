from random import randint

n = randint(0, 5)
chute = int(input('Adivinhe o número inteiro entre 0 e 5: '))

print('-=-' * 10)
if chute == n:
    print('Parabéns! Você acertou o número!!!')
else:
    print(f'Você perdeu! O número era {n}!')
print('-=-' * 10)


######### Forma simplificada #########

'''
print(f'Parabéns, você acertou o número!!!' if chute == n else f'Você errou! O número era {n}.' .format(n))
'''
