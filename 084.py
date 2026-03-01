pessoas = [
    ['Lincoln', 100],
    ['Camila', 50]
]
continuar = 'Sim'

# while continuar[0] != 'N':
#     nome = input('Digite o nome do pessoa: ')
#     peso = float(input('Digite o peso do pessoa: '))
#     pessoas.append([nome, peso])
#
#     continuar = input('Deseja continuar? Digite "não" para sair: ').strip().upper() or 'S'

peso_max = max(pessoas, key=lambda pessoa: pessoa[1])
print(f'O maior peso é {peso_max}')

peso_min = min(pessoas, key=lambda pessoa: pessoa[1])
print(f'O menor peso é {peso_min}')
