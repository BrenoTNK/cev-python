############ Modularização ############


# É recomendado usar assim, pois pode haver conflito com outros modulos;
# import _uteis        


# num = int(input('Digite um valor: '))
# fat = _uteis.fatorial(num)
# print(f'O fatorial de {num} é {fat}')
# print(f'O dobro de {num} é {_uteis.dobro(num)}')
# print(f'O triplo de {num} é {_uteis.triplo(num)}')



############ Pacotes ############
# São varias funções em modulos separados por assuntos
# Todo pacote tem um arquivo chamado __init__

from p_uteis import numeros
