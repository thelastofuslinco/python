import modules.moeda as moeda

numero = int(input('Digite um numero: '))

dobro = moeda.dobro(numero)
metade = moeda.metade(numero)
aumentar = moeda.aumentar(numero, 10)
diminuir = moeda.diminuir(numero, 10)

print(f'Aumentando 10% em {numero} temos {moeda.moeda(aumentar)}')
print(f'Diminuir 10% em {numero} temos {moeda.moeda(diminuir)}')
print(f'O dobro de {numero} é {moeda.moeda(dobro)}')
print(f'Metade de {numero} é {moeda.moeda(metade)}')
