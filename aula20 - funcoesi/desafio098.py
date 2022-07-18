from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 30)

    if passo == 0: passo = 1
    if passo < 0: passo *= (-1)

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)

    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ', flush=True)
            sleep(1)
    else:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ', flush=True)
            sleep(1)     

    ########## Com while ao inves de for ##########

    # count = inicio
    # if inicio < fim:
    #     while count <= fim:
    #         print(count, end=' ', flush=True)
    #         count += passo
    #         sleep(1)
    # else:
    #     while count >= fim:
    #         print(count, end=' ', flush=True)
    #         count -= passo
    #         sleep(1)

    print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalisar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
