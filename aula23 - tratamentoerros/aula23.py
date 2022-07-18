try:
    # Operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    # Erro de valor ou de tipo
    print('ERRO! Tipo de dados inválidos')
except ZeroDivisionError:
    # Erro se dividir por 0
    print('ERRO! Não se pode dividir por 0')
except KeyboardInterrupt:
    # Se não for digitado nada
    print('ERRO! Nada foi informado')
except Exception as erro:
    # Erros em geral
    print(f'ERRO! {erro.__cause__}')    # Mostra qual foi a causa
else:
    # Se deu certo
    print(f'O resultado é {r}')
finally:
    # Vai acontecer se deu certo ou não
    print('Volte sempre.')
