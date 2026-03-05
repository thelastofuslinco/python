tupla = tuple()
dicionario = dict()
lista = list()

print(f'Tupla {tupla}')
print(f'Dicionario {dicionario}')
print(f'Lista {lista}')

pessoas = list()
pessoas.append({
    'nome': 'Lincoln',
    'sexo': 'Masculino',
    'idade': 18
})
pessoas.append({
    'nome': 'Gustavo',
    'sexo': 'Masculino',
    'idade': 18
})

for pessoa in pessoas:
    for k, v in pessoa.items():
        print(f'{k} = {v}')
