numbers = []

while True:
    n = int(input('Digite um numero: '))
    numbers.append(n)
    question = input('Deseja continuar? [S/N] ').strip().upper()
    if question[0] == 'N':
        break

media = sum(numbers) / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print(f'A media é {media}')
print(f'O maximo é {maximum}')
print(f'O minimo é {minimum}')
