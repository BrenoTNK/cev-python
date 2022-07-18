nome = str(input('Digite o nome da cidade: ')).strip()

print('O nome da cidade começa com "SANTO"? {}' .format(nome[:5].upper() == 'SANTO'))


########## Com 'if' ##########

'''
print('O nome da cidade possui "SANTO".' if 'SANTO' in nome else 'O nome da cidade NÃO possui "SANTO".')
'''
