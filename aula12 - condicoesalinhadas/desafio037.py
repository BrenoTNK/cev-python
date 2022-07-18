num = int(input('Digite um número: '))
print('-=-' * 7)
print('1 - Binário.')
print('2 - Octal.')
print('3 - hexadecimal')
print('-=-' * 7)
base = int(input('Digite o número para conversão: '))

print('-=-' * 12)
if base == 1:
    valor = format(num, "b")        # bin(num)[2:]
    print(f'O número {num} convertido em BINÁRIO é {valor}')
elif base == 2:
    valor = format(num, "o")        # oct(num)[2:]
    print(f'O número {num} convertido em OCTAL é {valor}')
elif base == 3:
    valor = format(num, "x")        # hex(num)[2:]
    print(f'O número {num} convertido em HEXADECIMAL é {valor}')
else:
    print('Você digitou um valor inválido!!')
print('-=-' * 12)
