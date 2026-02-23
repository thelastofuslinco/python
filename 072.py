numbers = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    n = int(input('Digite um numero entre 0 e 10: '))

    if n < 0 or n > 10:
        print('Digite um numero entre 0 e 10')
    else:
        print(f'Voce digitou {numbers[n]}')
        break
