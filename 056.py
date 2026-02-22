class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


people = []

for index in range(4):
    people.append(Person(
        input('Qual o seu nome? '),
        int(input('Qual a sua idade? ')),
        input('Qual o seu sexo? [M/F] ')
    ))

media = sum(person.age for person in people) / len(people)
print(f'A media de idade do grupo é {media}.')

men = [person for person in people if person.sex.upper() == 'M']
if men:
    oldest_man = max(men, key=lambda person: person.age)
    print(f'O nome do homem mais velho é {oldest_man.name}.')
else:
    print('Não há homens no grupo.')

women_under_20 = sum(
    1 for person in people
    if person.sex.upper() == 'F' and person.age < 20
)
print(f'{women_under_20} mulheres tem menos de 20 anos.')
