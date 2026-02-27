numbers = list()
print(numbers)

for index in range(4):
    numbers.append(int(input(f'Digite um valor para a posição {index}: ')))
print(f'Voce digitou os valores {numbers}')

maior = numbers[0]
for number in numbers:
    if number > maior: maior = number
print(f'O maior numero digitado foi {maior} na posição {numbers.index(maior)}')
menor = numbers[0]
for number in numbers:
    if number < menor:
        menor = number
print(f'O menor numero digitado foi {menor} na posição {numbers.index(menor)}')
