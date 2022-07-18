frase = 'Curso em Vídeo Python'

print(frase)
print(frase[9])         # Encontra a letra 9 (Começa em 0);
print(frase[9:13])      # Encontra as letras de 9 a 13 (Esse último número não é incluido); 
print(frase[9:21:2])    # Encontra as letras de 9 a 21, pulando de 2 em 2;
print(frase[:5])        # Encontra as letras do começo até 5;
print(frase[15:])       # Encontra as letras de 15 até o final;
print(frase[9::3])      # Encontra as letras de 9 até o final, pulando de 3 em 3;

print(len(frase))               # Conta quantos caracteres tem a frase;
print(frase.count('o'))         # Conta quantos 'o's tem a frase;
print(frase.count('o', 0, 13))  # Conta quantos 'o's tem de 0 a 13;
print(frase.find('deo'))        # Mostra onde começa a palavra 'deo';
print(frase.find('Android'))    # Caso não exista a palavra, mostra -1;

print('Curso' in frase)         # Mostra se existe essa palavra;

print(frase.replace('Python', 'Android'))   # Substitui uma palavra que exista por outra;

print(frase.upper())            # Coloca tudo maiusculo;
print(frase.lower())            # Coloca tudo minusculo;
print(frase.capitalize())       # Coloca a primeira letra da frase em maiusculo;
print(frase.title())            # Coloca a primeira letra de cada palavra em maiusculo;
print(frase.split())            # Separa cada palavra e faz uma lista;
print('-'.join(frase.split()))  # Coloca um '-' separando cada item. (Se for uma frase é em cada caracter);


'''
frase = '   Aprenda Python  '

print(frase)
print(frase.strip())    # Tira todos os espaços desnecessarios no começo e no fim da frase;
print(frase.rstrip())   # Tira todos os espaços desnecessarios no final da frase;
print(frase.lstrip())   # Tira todos os espaços desnecessarios no começo da frase;
'''
