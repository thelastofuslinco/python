numeros = [[], []]

for c in range(11):
    n = int(input('Digite um numero: '))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print(f'A lista é {numeros}')
print(f'Os numeros impares {sorted(numeros[1])}')
print(f'Os numeros pares {sorted(numeros[0])}')
