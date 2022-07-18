from random import randint

nums = (
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10)
)

print('-=' * 20)
print('O valores sorteados foram: ', end = '')
for i in nums:
    print(i, end = ' ')
print('\n', '-=' * 20)
print(f'O maior número sorteado foi {max(nums)}')
print(f'O menor número sorteado foi {min(nums)}')
print('-=' * 20)
