def leaint(msg):
    while True:
        numero = str(input(msg))
        
        if numero.isnumeric():
            inteiro = int(numero)
            return inteiro
        else:
            print('error digite um numero valido')


n = leaint('Digite um numero: ')
print(f'O numero digitado foi {n}')
