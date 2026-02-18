name = input('Digite seu nome: ')

has_silva = name.upper().find('SILVA') != -1

if has_silva:
    print('Tem silva')
else:
    print('Tem não')
