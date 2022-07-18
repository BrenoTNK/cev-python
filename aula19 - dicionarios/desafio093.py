jogador = {}
gols_par = []

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gols_par.append(int(input(f'Quantos gols na partida {i}? ')))

jogador['gols'] = gols_par[:]
jogador['total'] = sum(gols_par)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for p, j in enumerate(jogador['gols']):
    print(f'    => Na partida {p} fez {j} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
