lanche = 'hamburguer', 'pizza', 'suco', 'pudim', 'batata frita'

for index in range(len(lanche)):
    print(f'lanche: {lanche[index]}, index: {index}')
print('\n')

for comida in lanche:
    print(f'lanche: {comida}')
print('\n')

for comida in lanche[:]:
    print(f'lanche: {comida}')
print('\n')

for index, comida in enumerate(lanche):
    print(f'lanche: {comida}, index: {index}')

a = 1, 2, 3, 4
b = 5, 6, 7, 8
c = a + b

print(a, b, c)
