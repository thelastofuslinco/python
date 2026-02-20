distancia = int(input('Qual a distancia em km: '))

if distancia <= 200:
    print(f'O preço da passagem ficou em {distancia * 0.50}.')
else:
    print(f'O preço da passagem ficou em {distancia * 0.45}')
