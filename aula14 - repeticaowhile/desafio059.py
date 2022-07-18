from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))

cod = 0
while cod != 5:
    print('-=' * 5, 'COMANDOS', '-=' * 5)
    print('''
    [1] Somar.
    [2] Multiplicar.
    [3] Maior.
    [4] Novos números.
    [5] Sair do programa.
    ''')
    print('-=' * 15)
    cod = int(input('Digite o número do comando: '))
    print('-=' * 15)

    if cod == 1:
        print(f'{n1} + {n2} = {n1 + n2}.')
    elif cod == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif cod == 3:
        if n1 > n2:
            print(f'O maior número é {n1}.')
        elif n2 > n1:
            print(f'O maior número é {n2}.')
        else:
            print(f'Os valores são iguais! {n1}.')
    elif cod == 4:
        n1 = int(input('Digite um novo primeiro valor: '))
        n2 = int(input('Digite um novo segundo valor: '))
    elif cod == 5:
        break
    else:
        print('-=' * 15)
        print('Valor inválido! Tente novamente!')
    sleep(3)

print('FIM DO PROGRAMA!')
print('-=' * 15)
