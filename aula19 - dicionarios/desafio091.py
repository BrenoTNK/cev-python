from random import randint
from time import sleep

dicio = {
    'jogador1' : randint(1, 6),
    'jogador2' : randint(1, 6),
    'jogador3' : randint(1, 6),
    'jogador4' : randint(1, 6)
}

print('Valores sorteados:')
for k, v in dicio.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(1)

print('-=' * 20)
print('  == RANKING DOS JOGADORES == ')
for p, i in enumerate(sorted(dicio, key = dicio.get, reverse=True)):      # Organiza o dicionário com os valores das chaves;
    print(f'    {p + 1}° lugar: {i} com {dicio[i]}')
    sleep(1)
