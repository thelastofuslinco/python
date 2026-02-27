numbers = []

for i in range(5):
    n = int(input('Digite um numero: '))
    inserted = False
    for j in range(len(numbers)):
        if n <= numbers[j]:
            numbers.insert(j, n)
            inserted = True
            break

    if not inserted:
        numbers.append(n)

    print(f'Lista atual: {numbers}')

print(f'Lista final em ordem crescente: {numbers}')
