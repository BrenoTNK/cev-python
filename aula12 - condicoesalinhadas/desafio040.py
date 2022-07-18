nota1 = float(input('Digite a 1° nota do aluno: '))
nota2 = float(input('Digite a 2° nota do aluno: '))

media = (nota1 + nota2) / 2

print('-=-' * 15)
print(f'Com notas {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}.')
if media < 5:
    print('Aluno REPROVADO!')
elif media >= 7:
    print('Aluno APROVADO!')
else:
    print('Aluno RECUPERAÇÃO!')
print('-=-' * 15)
