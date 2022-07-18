expre = str(input('Digite uma expressão'))
lista = []

for i in expre:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

print('Expressão válida!' if len(lista) == 0 else 'Expressão inválida!')


    ######### Solução meio gambiarra #########
'''
expre = list(map(str, input('Digite uma expressão: ')))

confirmador = False
if expre.count('(') == expre.count(')') and expre.index('(') < expre.index(')'):
    confirmador = True
    for i, valor in enumerate(expre):
        if valor == '(' and ')' in expre[i:]:
            confirmador = True
        else:
            confirmador = False
            break

print('Expressão válida!' if confirmador == True else 'Expressão inválida!')
'''
