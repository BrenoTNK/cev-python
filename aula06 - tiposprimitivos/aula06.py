n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2

# print('A soma vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

########################

n = input('Digite algo: ')
print(n.isnumeric())    # Se é númerico;
print(n.isalpha())      # Se é letra;
print(n.isalnum())      # Se é alfanumerico;
print(n.isupper())      # Se está só maiusculo;
print(n.islower())      # Se está só minusculo;
