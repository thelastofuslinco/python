number = int(input('Digite o numero: '))

for i in range(1, 11):
    print('{} / {:2} = {}'.format(number, i, number/i))

for i in range(1,11):
    print('{} + {} = {}'.format(number,i,number+i))

print('\n')

for i in range(1, 11):
    print('{} x {:2} = {}'.format(number, i, number*i))