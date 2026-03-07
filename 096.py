def area(a, b):
    print(f'{'Controle de terrenos':^40}')
    print('-' * 40)
    print(f'comprimento {a}m X largura {b}m')
    print(f'area = {a * b:.0f}m²')
    print('-' * 40)


comprimento = float(input('Qual a sua comprimento: '))
largura = float(input('Qual a sua largura: '))

area(4.5, 8)
