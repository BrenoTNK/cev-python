lista = []
aluno = []
notas = []

while True:
    aluno.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 1: ')))

    aluno.append(notas[:])
    media = (aluno[1][0] + aluno[1][1]) / 2
    aluno.append(media)
    notas.clear()

    lista.append(aluno[:])
    aluno.clear()

    while True:
        cod = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if cod in 'SN': break
    if cod == 'N': break

print('-=' * 15)
print(f'No. {"NOME":15} MÉDIA')
print('--' * 15)
for num, al in enumerate(lista):
    print(f'{num:<4} {al[0].capitalize():<15} {al[2]:5>.1f}')
print('-=' * 15)

while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999: break
    print(f'Notas de {lista[mostrar][0].capitalize()} são {lista[mostrar][1]}')
    print('-=' * 15)

print('-=' * 15)
print('FINALIZADO!!')
print('-=' * 15)
