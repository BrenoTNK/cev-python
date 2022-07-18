pessoas = {
    'nome' : 'Gustavo',
    'sexo' : 'M',
    'idade' : 22
}
print(pessoas)
print(pessoas['nome'])      # Mostra apenas o valor na chave 'nome';
print(pessoas['idade'])     # Mostra apenas o valor na chave 'idade';
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de idade.')
print(pessoas.keys())       # Mostra as chaves;
print(pessoas.values())     # Mostra os valores;
print(pessoas.items())      # Mostra as chaves com os valores;

for k in pessoas.keys():
    # Apenas chave;
    print(k)
for v in pessoas.values():
    # Apenas valor;
    print(v)
for k, v in pessoas.items():
    # Chave e valor;
    print(f'{k} = {v}')

del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5


brasil = []
estado1 = { 'uf' : 'Rio de Janeiro', 'sigla' : 'RJ' }
estado2 = { 'uf' : 'São Paulo', 'sigla' : 'SP' }
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])


estado = dict()
brasil = list()
for i in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(f'{v}', end = ' ')
    print()
