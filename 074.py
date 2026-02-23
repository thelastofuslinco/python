import random

numbers = (
    random.randint(0, 10),
    random.randint(0, 10),
    random.randint(0, 10),
    random.randint(0, 10),
    random.randint(0, 10),
)

print(f'Os numeros sorteados são {numbers}')

maior = numbers[0]
for index in range(0, len(numbers)):
    number = numbers[index]
    if number > maior:
        maior = number
print(f'O maior numero sorteado foi {maior}')

menor = numbers[0]
for index in range(0, len(numbers)):
    number = numbers[index]
    if number < menor:
        menor = number
print(f'O menor numero sorteado foi {menor}')
