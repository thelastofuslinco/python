import random


def sortear(value):
    for index in range(5):
        value.append(random.randint(0, 9))
    print(f'Os valores sorteados foram {value}')


def soma_par(values):
    aux = []
    for value in values:
        if value % 2 == 0:
            aux.append(value)
    print(f'A soma de todos os valores {aux} é {sum(aux)}')


numbers = []

sortear(numbers)
soma_par(numbers)
