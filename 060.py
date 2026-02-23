fatorial = int(input('Qual o fatorial de um numero?: '))
contador = 1
print(f'Com while antes: {contador}')
while fatorial > 0:
    contador = contador * fatorial
    fatorial -= 1

print(f'Com while depois: {contador}')

contador = 1
print(f'Com for antes: {contador}')
for c in range(1, 6):
    contador = contador * c
print(f'Com for {contador}')
