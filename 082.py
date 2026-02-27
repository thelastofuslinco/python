numbers = []

while True:
    n = int(input('Digite um numero ou 999 para parar: '))

    if n == 999:
        break
    numbers.append(n)

print(numbers)
print(f'pares: {[number for number in numbers if number % 2 == 0]}')
print(f'impares: {[number for number in numbers if number % 2 != 0]}')
