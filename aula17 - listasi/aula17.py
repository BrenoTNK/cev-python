num = [2, 5, 9, 1]
num[2] = 3                  # Subistiu o valor no elemento '2' pelo 3;
num.append(7)               # Adiciona um novo valor a lista;
num.sort()                  # Coloca em ordem crescente;
num.sort(reverse=True)      # Coloca em ordem decrescente;
num.insert(2, 0)            # Coloca um valor no meio da lista sem sobrepor o outro;
print(len(num))             # Lê quantos elementos possui;
num.pop()                   # Remove o último valor da lista;
num.pop(2)                  # Remove o valor '2' determinado;
num.remove(2)               # Remove o primeiro elemento com valor '2';


valores = []
for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for v in valores:
    print(f'{v}... ', end = '')
print('FIM!')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Fim da lista.')


a = [2, 3, 4, 7]
b = a       # Assim, há ligação entre as duas listas (alterar uma, altera a outra);
b = a[:]    # Assim, cria uma copia dos valores da lista para outra;
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
