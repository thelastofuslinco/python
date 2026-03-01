matriz = []
matiz_range = 3

for linha in range(matiz_range):
    matriz.append([])
    for coluna in range(matiz_range):
        matriz[linha].append(int(input('Digite um valor: ')))

for linha in matriz:
    for coluna in linha:
        print(f'[{coluna}] ', end='')
    print('')
