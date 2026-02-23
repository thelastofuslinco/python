numbers = []
while True:
    n = int(input('Digite um numero: '))

    if n == 999:
        break
    
    numbers.append(n)
print(f'Foram digitados {len(numbers)} a soma deles é {sum(numbers)}')
