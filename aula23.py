# Tramento de erros
try:
    numerador = int(input('Digite um numero: '))
    denominador = int(input('Digite um denominador: '))
    resultado = numerador / denominador
except (TypeError, ValueError):
    print('Erro no tipo de dados.')
except ZeroDivisionError:
    print('Divisão por zero nao permitido.')
except KeyboardInterrupt:
    print('Programa foi interrompido.')
except Exception as erro:
    print(f'Erro: {erro}')
else:
    print(f'O resultado é {resultado}')
finally:
    print('Volte sempre!')
