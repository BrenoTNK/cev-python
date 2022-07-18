# help(print)               // Mostra mais informações sobre a funcionalidade;
# print(input.__doc__)      // Mesma coisa;



########### (Interactive Help) ########### 
    # Criar um help para um função criada no programa;
def contador(inicio, fim, passo):
    """
    -> Faz um cantagem e mostra na tela.
    :param inicio: início da contagem
    :param fim:    fim da contagem
    :param passo:  passo da contage
    :return:       sem retorno
    """
    for c in range(inicio, fim + 1, passo):
        print(c, end=' ', flush=True)
    print('FIM!')
help(contador)



########### (Parâmetros Opcionais) ###########

def somar(a=0, b=0, c=0):
    # Parâmetro(s) recebendo um valor ele vira um parâmetro opcional;
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(8, 4)
somar()
somar(c=3, a=8)



########### (Escopo de Variáveis) ###########

def testei():
    x = 8   # Variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2       # Variável global
print(f'No programa principal, n vale {n}')
testei()
    # O 'x' ele está somente dentro da função teste()
    # então, não irá funcionar fora dessa função
# print(f'No programa principal, x vale {x}')

#################################

def testeii(b):
    a = 8       # Não é o "a" global, é criado um "a" local valendo 8.
    b += 4
    c = 2
    print(f'Dentro de testeii - A = {a}, B = {b}, C = {c}')


a = 5
print(f'Fora - A = {a}')
testeii(a)

#################################

def testeiii(b):
    global a
    a = 8       # Agora sim é o "a" global.
    b += 4
    c = 2
    print(f'Dentro de testeiii - A = {a}, B = {b}, C = {c}')


a = 5
testeiii(a)
print(f'Fora - A = {a}')



########### (Retorno de Valores) ###########

def somari(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somari(3, 2, 5)
r2 = somari(2, 2)
r3 = somari(6)
print(f'Os resultados foram {r1}, {r2} e {r3}.')


########### Pratica ###########

def fatorial(num=1):
    # Fatorial de um número;
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

######################

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um números: '))
print('É par!' if par(num) is True else 'Não é par!')
