expressao = '((a+b) * c)'

aberto = expressao.count('(')
fechado = expressao.count(')')

if aberto - fechado == 0:
    print('Expressao correta')
else:
    print('Expressao errada')
