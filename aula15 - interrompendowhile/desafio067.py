while True:
    n = int(input('Quer ver a tabuada de qual valor? (Negativo para parar): '))
    print('-=' * 25)

    if n < 0:
        break

    for i in range(1, 11):
        print(f'{n} x {i:2} = {n * i}')
    print('-=' * 25)

print('Programa encerrado!')
