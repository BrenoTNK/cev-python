print('Confirmador de palíndromo.')
frase = str(input(('Digite uma frase sem acento ou pontuação: '))).strip().lower()
frase = frase.replace(' ', '')
inverso = ''

# inverso = frase[::-1]     // Sem precisar do for
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]

print(f'Você digitou {frase}. Invertido fica {inverso}.')
print('-=' * 14)
print('Essa frase é palíndromo!' if frase == inverso else 'Essa frase NÃO é palíndromo!')
print('-=' * 14)
