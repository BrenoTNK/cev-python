lanche = ('Hambúrguer', 'Suco', 'Piza', 'Pudim', 'Batata Frita')

print(lanche)           # Mostra todos;
print(lanche[1])        # Elemento 1;
print(lanche[3])        # Elemento 3;
print(lanche[-2])       # Penúltimo elemento;
print(lanche[1:3])      # Do elemento 1 ao 3 (o 3 não conta);
print(lanche[2:])       # Do elemento 2 até o fim;
print(lanche[:2])       # Do começo até o elemento 2;
print(lanche[-2:])      # Do penúltimo elemento até o final;
print(lanche[-3:])      # Do antepenúltimo elemento até o final;

    # Tuplas são imutáveis
# lanche[1] = 'Refrigerante'    // Não funciona;


for comida in lanche:
    print(f'Eu vou comer {comida}')

for count in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[count]} na posição {count}')

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na poisção {pos}')

print(sorted(lanche))       # Mostra em ordem alfabetica;


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))           # Lê quantos elementos possui a tupla;
print(c.count(5))       # Conta quantos '5' tem a tupla;
print(c.index(5))       # Mostra a posição do primeiro '5' na tupla;
print(c.index(5, 1))    # Mostra a posição do primeiro '5' a partir da posição 1;

pessoa = ('Gustavo', 39, 'M', 99.88)    # Aceita strings e números na tupla;
del(pessoa)         # Pode apagar uma tupla inteira;
