lista = []
jogador = {}

while True:
    # Leitura dos dados do jogador;
    total = 0
    gols = []

    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for g in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {g + 1}: ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())

    while True:
        # Se quer continuar cadastrando jogadores;
        cod = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if cod in 'SN': break
        print('--' * 30)
        print('ERRO! Por favor, digite apenas S ou N.')
    if cod == 'N': break
    print('--' * 30)

print('-=' * 30)
print(lista)
print('--' * 30)
print('cod ', end = '')
for i in jogador.keys():
    # Cabeçalho;
    print(f'{i:<15} ', end = '')
print()
print('--' * 30)
for k, v in enumerate(lista):
    # Mostrar dados dos jogadores;
    print(f'{k:>3} ', end = '')
    for j in v.values():
        print(f'{str(j):<15} ', end = '')
    print()
print('-=' * 30)

while True:
    # Escolher um jogador para mostrar dados mais especificos;
    cod = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if cod == 999: break

    if cod >= len(lista):
        print('--' * 30)
        print(f'ERRO! Não existe jogador com código {cod}! Tente novamente!')
    else:
        print(f'-- LEVANTAMENTO DE JOGADOR {lista[cod]["nome"]} --')
        for p, j in enumerate(lista[cod]['gols']):
            # Mostrar as partidas e os gols do jogador;
            print(f'    No jogo {p + 1} fez {j} gols.')
    print('--' * 30)

print('-=' * 30)
print(f'{"-=-=-=- FIM DO PROGRAMA -=-=-=-":^60}')
