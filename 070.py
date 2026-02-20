products = []

while True:
    product_name = input('Informe o nome do produto: ')
    product_price = float(input('Informe o valor do produto: '))

    products.append({'name': product_name, 'price': product_price})

    while True:
        is_true = input('Deseja continuar? [S/N] ').strip().upper()

        if is_true in ('S', 'N'):
            break
        print('Resposta errada! Digite apenas S ou N')

    if is_true == 'N':
        break

print(f'Total de gastos: {sum(product['price'] for product in products)}')
print(f'{len(list(filter(lambda product: product['price'] > 1000, products)))} produtos custam mais de 1000')
print(f'Produto mais barato {sorted(products, key=lambda product: product['price'])[0]["name"]}')
