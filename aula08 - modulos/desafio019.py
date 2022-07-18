from random import choice

nome1 = str(input('Digite o nome do 1° aluno: '))
nome2 = str(input('Digite o nome do 2° aluno: '))
nome3 = str(input('Digite o nome do 3° aluno: '))
nome4 = str(input('Digite o nome do 4° aluno: '))
lista = [nome1, nome2, nome3, nome4]

sorteado = choice(lista)

print('O(A) {} foi sorteado para limpar o quadro.'.format(sorteado))


############# 2° maneira #############
'''
lista = list(range(4))
i = 0
for i in lista:
    lista[i] = input('Digite o nome do aluno: ')

print('O(A) {} foi sorteado para limpar o quadro.'.format(choice(lista)))
'''
