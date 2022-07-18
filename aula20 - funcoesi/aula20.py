def soma(a, b):
    # Função para não ficar repetindo código;
    print(f'A = {a} + B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


    # Programa principal;
soma(4, 5)
soma(a=8, b=9)      # Especificar os valores;
soma(b=2, a=1)      # Se especificar um, os outros também tem;



def contador(* num):
    # O * deixa colocar varios parametros;
    print(num)


contador(3, 4 ,5)
contador(4, 7, 9, 0, 1)
contador(1)



def dobrar(lst):
    # vai dobrar cada valor da lista;
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [3, 5, 1, 0, 7, 6]
dobrar(valores)
print(valores)



def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(7, 2)
soma(4, 10, 5, 1)
