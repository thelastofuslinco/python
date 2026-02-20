def print_table(n):
    print('-' * 30)
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 30)


def multiplication_table(n):
    if n <= -1:
        return 0
    if n != 0:
        print_table(n)
    n = int(input('Digite um numero: '))
    multiplication_table(n)


multiplication_table(0)
