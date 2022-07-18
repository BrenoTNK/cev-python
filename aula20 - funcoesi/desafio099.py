from time import sleep


def maior(*num):
    count = mai = 0
    print('-=' * 40)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(1)
        if count == 0:
            mai = valor
        else:
            if valor > mai: mai = valor
        count += 1
    print(f'Foram informados {count} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


# Programa principal
maior(6, 9, 2, 5, 1)
maior(0, 7, 2, 1)
maior(2, 1)
maior(4)
maior()
