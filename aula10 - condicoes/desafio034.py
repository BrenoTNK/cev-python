salario = float(input('Digite o salário do funcionário - R$ '))

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

print(f'O novo salário do funcionario é de R${aumento:.2f}.')
