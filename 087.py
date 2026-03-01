matriz = []
matiz_range = 3

for linha in range(matiz_range):
    matriz.append([])
    for coluna in range(matiz_range):
        matriz[linha].append(int(input('Digite um valor: ')))
soma_par = 0

for linha in matriz:
    for coluna in linha:
        print(f'[{coluna}] ', end='')

        if coluna % 2 == 0:
            soma_par += coluna
    print('')

terceira_coluna_total = 0

for linha in range(matiz_range):
    terceira_coluna_total += matriz[linha][2]

print(f'A soma de todos os valores pares: {soma_par}')
print(f'A soma dos valores da terceira coluna: {terceira_coluna_total}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')
