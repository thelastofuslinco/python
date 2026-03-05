pessoas = []

while True:
    usuario = {}
    usuario['nome'] = str(input('Nome: '))
    usuario['idade'] = int(input('Idade: '))
    usuario['sexo'] = str(input('Sexo [M/F]: ')).upper()
    pessoas.append(usuario)

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

idade_media = sum([pessoa['idade'] for pessoa in pessoas]) / len(pessoas)

print(f'O total de pessoas cadastradas sao {len(pessoas)}')
print(f'A media de idade do grupo é {idade_media}')
print(f'O total de mulheres no grupo é de {len([pessoa for pessoa in pessoas if pessoa['sexo'] == 'F'])}')
print(
    f'O total de pessoas acima da idade media é de {len([pessoa for pessoa in pessoas if pessoa['idade'] >= idade_media])}')
