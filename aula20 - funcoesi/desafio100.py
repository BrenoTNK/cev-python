from random import randint
from time import sleep

lista = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[i]} ', end='', flush=True)
        sleep(1)
    print('PRONTO!')


def somaPar(valores):
    soma = 0
    for i in valores:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {valores}, temos {soma}')


# Programa principal
sorteia()
somaPar(lista)
