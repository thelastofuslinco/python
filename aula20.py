def message(msg):
    print('-' * 30)
    print(f'{msg.upper().strip():^30}')
    print('-' * 30)


message('Titulo')
message('Descrição')
message('Valor')


def somar(a=0, b=0):
    print(f'A soma de A = {a} e B = {b} é {a + b}')


somar(4, 5)
somar(b=2, a=3)


def contador(*values):
    for value in values:
        print(f'{value} -> ', end='')
    print()


contador(1, 2, 3)
contador(1, 2, 3, 4, 5)
