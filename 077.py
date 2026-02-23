palavras = (
    'APRENDER',
    'PROGRAMAR',
)

for palavra in palavras:
    vogais = 'aeiou'
    lista = [char for char in palavra.strip().lower() if char in vogais]
    print(f'Na palavra {lista}')
