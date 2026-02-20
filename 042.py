a = float(input('Qual o valor da primeira linha: '))
b = float(input('Qual o valor da segunda linha: '))
c = float(input('Qual o valor da terceira linha: '))

is_triangle = ((b - c) < a < (b + c)) and ((a - c) < b < (a + c)) and ((b - c) < a < (b + c))

if is_triangle:
    print('Pode formar um triangulo')

    if a == b == c:
        print('equilatero')
    elif a == b or a == c or b == c:
        print('isosceles')
    else:
        print('escaleno')
else:
    print('Não pode formar um triangulo')
