play = True

while play:
    player_even_or_odd = input('Digite impar ou par: ')
    player_number = int(input('Digite um numero: '))

    machine_number = 1
    numbers_sum = machine_number + player_number

    if numbers_sum % 2 == 0:
        print(f'somando {numbers_sum} Par')
        if player_even_or_odd != 'par':
            print('Perdeu!')
            break
        print('Ganhou!')
    else:
        print(f'somando {numbers_sum} Impar')
        if player_even_or_odd != 'impar':
            print('Perdeu!')
            break
        print('Ganhou!')
