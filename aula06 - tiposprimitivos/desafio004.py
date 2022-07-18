texto = input('Digite algo: ')

print('É alfabetico:', texto.isalpha())
print('É um número:', texto.isnumeric())
print('É alfanumerico:', texto.isalnum())
print('Está em maiusculo:', texto.isupper())
print('Está em minusculo:', texto.islower())
print('Está capitalizado:', texto.istitle())
print('Só é espaço:', texto.isspace())
