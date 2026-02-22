numbers = []
result = 0

for index in range(0, 6):
    numbers.append(int(input('digite um numero: ')))

for number in numbers:
    if number % 2 == 0:
        result += number
print(result)
