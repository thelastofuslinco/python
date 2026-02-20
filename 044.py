valor = float(input('Qual o valor do produto: '))
forma_pagamento = input('Qual a forma de pagamento: ')

if forma_pagamento == 'cartao': parcelas = int(input('Quantos parcelas? '))

if forma_pagamento == 'dinheiro' or forma_pagamento == 'cheque':
    print(f'Valor do produto: {valor} 10% de desconto fica {valor * 0.90}')
if forma_pagamento == 'cartao':
    if parcelas == 1:
        print(f'Valor do produto: {valor} 5% de desconto fica {valor * 0.95}')
    elif parcelas == 2:
        print(f'Valor do produto: {valor}')
    elif parcelas >= 3:
        print(f'Valor do produto: {valor} 20% de juros fica {valor * 1.20}')
