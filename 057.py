while True:
    sex = input('Digite seu sexo (M/F): ').upper().strip()

    if sex[0] == 'M' or sex[0] == 'F':
        break
    print('Erro: digite seu sexo (M/F)')
