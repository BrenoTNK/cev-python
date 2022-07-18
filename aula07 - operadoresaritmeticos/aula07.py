# +  adição
# -  subtração 
# *  multiplicação 
# /  divisão
# ** potência
# // divisão inteira
# %  resto da divisão
# == igual

# Ordem de precedência:
# 1° ()
# 2° **
# 3° * / // %
# 4° + -

################

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m,d))
print('Divisão inteira{} e potência {}'.format(di, e))

################

    # Extra:
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))      # Deixa 20 de espaço para o nome;
print('Prazer em te conhecer {:>20}!'.format(nome))     # Coloca o nome no final;
print('Prazer em te conhecer {:<20}!'.format(nome))     # Coloca o nome no começo;
print('Prazer em te conhecer {:^20}!'.format(nome))     # Coloca o nome no centro;
print('Prazer em te conhecer {:=^20}!'.format(nome))    # Coloca o nome no centro preenchendo o resto com '=';
