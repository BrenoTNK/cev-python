for i in range(1, 6):
    print(i)
print('FIM!')
for i in range(6, 0, -1):
    print(i)
print('FIM!')

n = int(input('Digite um número: '))
for i in range(0, n+1):
    print(i)
print('FIM!')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for i in range(i, f+1, p):
    print(i)
print('FIM!')

s = 0
for i in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores é {}!' .format(s))
