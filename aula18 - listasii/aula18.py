teste = list()
galera = list()
teste.append('Gustavo')
teste.append(40)
galera.append(teste[:])     # Adiciona uma cópia da lista;
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])     # Adiciona outra cópia da lista;
print(galera)



galera = [['João', 19], ['Ana', 33], ['Joaquim', 33], ['Maria', 45]]
print(galera)               # Mostra toda a lista;
print(galera[0])            # Mostra os dados do João;
print(galera[0][0])         # Mostra apenas o nome do João;
print(galera[2][1])         # Mostra a idade do Joaquim;

for pessoa in galera:   
    print(pessoa)       # Mostra todas as pessoas;
    print(pessoa[0])    # Mostra só os nomes das pessoas;
    print(pessoa[1])    # Mostra só a idade das pessoas;

    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')



galera = list()
dado = list()
maiores = menores = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade.')
        maiores += 1
    else:
        print(f'{i[0]} é menor de idade.')
        menores += 1

print(f'Temos {maiores} maiores e {menores} menores de idade.')
