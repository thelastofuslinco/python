import modules.moeda as moeda

numero = int(input('Digite um numero: '))

print(f'Aumentando 10% em {numero} temos {moeda.aumentar(numero, 10, True)}')
print(f'Diminuir 10% em {numero} temos {moeda.diminuir(numero, 10, True)}')
print(f'O dobro de {numero} é {moeda.dobro(numero, True)}')
print(f'Metade de {numero} é {moeda.metade(numero, True)}')
