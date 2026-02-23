numbers = (
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
)

print(f'O numero 9 apareceu {numbers.count(9)} vezes.')
print(f'O numero 3 apareceu na posição {numbers.index(3)}.')

par = [number for number in numbers if number % 2 == 0]
print(f'Os numeros pares são {len(par)}')
