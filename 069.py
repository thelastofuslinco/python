people = []

while True:
    age = int(input('Quantos anos tem? '))
    sex = input('Qual seu sexo? [M/F] ').strip().upper()

    while True:
        sex = input('Qual seu sexo? [M/F] ').strip().upper()
        if sex in ('M', 'F'):
            break
        print('Sexo inválido, digite apenas M ou F.')

    people.append({
        'age': age,
        'sex': sex
    })

    while True:
        is_true = input('Quer continuar? [S/N] ').strip().upper()
        if is_true in ('S', 'N'):
            break
        print('Resposta inválida, digite apenas S ou N.')
        
    if is_true == 'N':
        break

more_18 = list(filter(lambda person: person['age'] >= 18, people))
mans = list(filter(lambda person: person['sex'] == 'M', people))
woman_18 = list(filter(lambda person: (person['sex'] == 'F') and (person['age'] >= 18), people))

print(f'{len(more_18)} pessoas possuem 18 anos ou mais')
print(f'Foram cadastrados {len(mans)} homens')
print(f'{len(woman_18)} mulheres com mais de 18 anos foram cadastradas')
