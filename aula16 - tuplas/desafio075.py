nums = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)
print(f'Você digitou os valores {nums}')

print('-=' * 20)
print(f'O valor 9 apareceu {nums.count(9)} vezes.')
print(f'O valor 3 apareceu na {nums.index(3) + 1}° posição.' if 3 in nums else 'O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end = '')
for i in nums:
    if i % 2 == 0: 
        print(i, end = ' ')
print('\n', '-=' * 20)
