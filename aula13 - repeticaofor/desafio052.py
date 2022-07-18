n = int(input('Digite um número: '))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        # Número divisor fica amarelo;
        print('\033[33m', end = '')
        count += 1      # Conta quantos divisores possui;
    else:
        # Número não divisor fica vermelho;
        print('\033[31m', end = '')
    print(f'{i} ', end = '')

print(f'\n\033[mO número {n} foi divisível {count} vez(es).')
print('-=' * 12)
if count == 2:
    # Números primos só são divididos por 1 e ele mesmo;
    print('Então, ele É PRIMO!')
else:
    print('Então, ele NÃO É PRIMO!')
    # O 1 não é primo;
print('-=' * 12)
