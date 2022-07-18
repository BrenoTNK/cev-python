palavras = (
    'python', 'curso', 'programar', 'projeto', 'objeto',
    'tupla', 'estudar', 'mercado', 'trabalhar', 'futuro',
    'gratuito', 'aprender', 'computador', 'celular',
    'algoritmo', 'banco de dados', 'web', 'visualstudiocode'
)

for word in palavras:
    print(f'\nNa palavra {word.upper()} temos: ', end = '')
    for i in word:
        if i.lower() in 'aieou':
            print(i.lower(), end = ' ')
