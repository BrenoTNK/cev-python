from random import randint
from time import sleep

lista = []
jogos = []

print('-=' * 18)
print('{:^36}' .format('JOGOS NA  MEGA SENA'))
print('-=' * 18)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 4, f'SORTEANDO {quantidade} JOGOS', '-=' *4)
for i in range(0, quantidade):
    for nums in range(0, 6):
        n = randint(1, 60)
        if nums != 0:
            while n in jogos:
                n = randint(1, 60)
        jogos.append(n)
    jogos.sort()
    lista.append(jogos[:])
    print(f'Jogo {i + 1}: {jogos}')
    jogos.clear()
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
