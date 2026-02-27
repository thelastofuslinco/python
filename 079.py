numbers = []

while True:
    n = int(input('Digite um numero: '))
    if n not in numbers:
        numbers.append(n)

    option = input('Deseja continuar? [S/N] ').upper().strip()
    if option[0] == 'N':
        break

print(numbers)
