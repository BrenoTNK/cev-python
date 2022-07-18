from random import shuffle

nome1 = input('Digite o nome do 1° aluno: ')
nome2 = input('Digite o nome do 2° aluno: ')
nome3 = input('Digite o nome do 3° aluno: ')
nome4 = input('Digite o nome do 4° aluno: ')
lista = [nome1, nome2, nome3, nome4]

shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))


############# 2° maneira #############
'''
lista = list(range(4))
i = 0
for i in lista:
    lista[i] = input('Digite o nome do aluno: ')
shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))
'''
