n = s = 0
while True:
    # Loop infinito;
    n = int(input('Digite um número: '))
    if n == 999:
        # Para o loop;
        break
    s += n
print(f'A soma vale {s}')
