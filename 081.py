numbers = []

while True:
    n = int(input('Digite um numero: '))
    if n not in numbers:
        numbers.append(n)

    option = input('Deseja continuar? [S/N] ').upper().strip()
    if option[0] == 'N':
        break

print(f'Foram digitados {len(numbers)}')
print(f'A lista ordernada foi {sorted(numbers)}')
print('O numero 5 esta na lista' if 5 in numbers else 'O numero 5 não esta na lista')
