aluno = {}

aluno['nome'] = str(input('Nome do aluno: ')).capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] > 7:
    aluno['situação'] = 'Aprovado!'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação!' 
else:
    aluno['situação'] = 'Reprovado!'

print('-=' * 20)
for k, v in aluno.items():
    print(f'    - {k.capitalize()} é igual a {v}')
print('-=' * 20)
