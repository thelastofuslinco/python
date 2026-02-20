n = 0
array = []
while True:
    n = int(input('Digite um numero: '))
    if (n == 999):
        break
    array.append(n)
print(f'A soma dos {len(array)} valores é {sum(array)}.')
