city = input('Digite o nome da cidade: ')

starts_with = city.split()[0].upper().find('SANTO')

if starts_with != -1:
    print('Começa')
else:
    print('Não começa')
