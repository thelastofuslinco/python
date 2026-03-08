def leiaint(msg):
    while True:
        try:
            numero = int(input(msg).strip().replace(',', '.'))
            return numero
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um numero inteiro valido.\033[m')


def leiafloat(msg):
    while True:
        try:
            numero = float(input(msg).strip().replace(',', '.'))
            return numero
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um numero real valido.\033[m')


inteiro = leiaint('Digite um numero inteiro valido: ')
real = leiafloat('Digite um numero real: ')

print(f'O numero inteiro digitado foi {inteiro}')
print(f'O numero real digitado foi {real}')
