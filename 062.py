primeiro = int(input('digite o primeiro numero: '))
razao = int(input('Digite a razao: '))

index = 10
while index > 0:
    index -= 1
    print(f'{primeiro}')
    primeiro += razao

    if index == 0:
        index = int(input('Deseja ver quantas razoes?\ndigite 0 para sair: '))
