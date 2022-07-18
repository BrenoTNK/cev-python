tupla = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    n = int(input('Digite um número entre 0 e 20: '))

    #if n in range(0, len(tupla)):   // Se quiser aumentar a tupla sem alterar o codigo;
    if 0 <= n <= 20: break

    print('Número inválido! Tente novamente.')

print('-=' * 18)
print(f'Você digitou o número {tupla[n]}')
print('-=' * 18)


############## Bonûs - Pedir para o usuário se quer continuar ##############

'''
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))

        if 0 <= n <= 20: break

        print('Número inválido! Tente novamente.')
    print('-=' * 18)
    print(f'Você digitou o número {tupla[n]}')
    print('-=' * 18)

    while True:
        com = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if com in 'SN': break

    if com == 'N': break
print('FIM!')
'''
