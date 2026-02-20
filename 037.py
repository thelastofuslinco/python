number = int(input('Digite um numero: '))
type = input('Digite um tipo para a conversao binario, octal ou hexadecimal: ').lower().strip()

if type == 'binario':
    binario = ''
    decimal = number
    while decimal > 0:
        binario += str(decimal % 2)
        decimal = decimal // 2
    print(f'Inteiro {number}\nBinario {binario}')
elif type == 'octal':
    octal = ''
    decimal = number
    while decimal > 0:
        octal += str(decimal % 8)
        decimal = decimal // 8
    print(f'inteiro {number}\nOctal {octal[::-1]}')
elif type == 'hexadecimal':
    hexadecimal = ''
    digitos = "0123456789ABCDEF"
    decimal = number
    while decimal > 0:
        hexadecimal += digitos[decimal % 16]
        decimal = decimal // 16
    print(f'inteiro {number}\nHexadecimal {hexadecimal[::-1]}')
