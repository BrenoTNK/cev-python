from random import randint

venceu = 0

print('-=-=-=-=-=-=-= JOGO DE PAR OU ÍMPAR -=-=-=-=-=-=-=')
while True:
    paridade = ' '
    computador = randint(0, 11)

    jogador = int(input('Digite um valor: '))
    while paridade not in 'PpIi':
        paridade = str(input('Par ou Ímpar? [P/I]: ')).strip()[0]
    print('-=' * 15)

    soma = jogador + computador

    print(f'Você jogou {jogador} e o computador {computador}.')
    print(f'Total de {soma} DEU PAR!' if soma % 2 == 0 else f'Total de {soma} DEU ÍMPAR!')
    print('-=' * 15)

    if (soma % 2 == 0 and paridade in 'Ii') or (soma % 2 == 1 and paridade in 'Pp'):
        print('Você PERDEU!!')
        break

    venceu += 1
    print('Você VENCEU!!')
    print('Vamos jogar novamente...')
    print('-=' * 15)

print('-=' * 15)
print(f'GAME OVER! Você venceu {venceu} vezes.')
print('-=' * 15)
