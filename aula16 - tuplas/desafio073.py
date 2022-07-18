time = (
    'Palmeiras', 'Fluminense', 'Athletico-PR', 'Atlético-MG', 'Corinthians',
    'Internacional', 'São Paulo', 'Flamengo', 'Botafogo', 'Bragantino',
    'Goiás', 'Coritiba', 'Santos', 'América-MG', 'Avaí',
    'Ceará SC', 'Atlético-GO', 'Cuiabá', 'Juventude', 'Fortaleza'
)

print('-=' * 20)
print(f'Os 5 primeiros na tabela são: {time[:5]}')
print('-=' * 20)
print(f'os 4 últimos na tabela são: {time[-4:]}')
print('-=' * 20)
print(f'Os times em ordem alfabetica é: {sorted(time)}')
print('-=' * 20)
# No original o time é a Chapecoense, mas, atualmente, ela não está no campeonato;
print(f'O Bragantino está na {time.index("Bragantino") + 1}° posição.')
print('-=' * 20)
