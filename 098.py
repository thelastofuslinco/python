def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    print(f'De {inicio} até {fim} contando em {passo}')

    if inicio > fim and passo > 0 or inicio < fim and passo < 0:
        passo = -passo

    for c in range(inicio, fim, passo):
        print(c, end=' ')
    print('')


contador(1, 10, 1)  # menor, maior e positivo
contador(10, 1, 2)  # maior, menor e positivo
contador(10, 1, -2)  # maior, menor e negativo
contador(1, 10, -1)  # menor, maior e negativo
contador(1, 10, 0)  # menor, maior e zero
