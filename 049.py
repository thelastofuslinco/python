number = int(input('Digite um numero'))

print('multiplicação:')
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

print('\n')

print('divisao:')
for i in range(1, 11):
    print(f'{number} / {i} = {number / i:.2f}')

print('\n')

print('soma:')
for i in range(1, 11):
    print(f'{number} + {i} = {number + i}')
