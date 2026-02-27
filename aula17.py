numbers = list(range(10))
print(numbers)

# del numbers[1] // remove 2
# numbers.pop(1) // remove 2
# numbers.remove(2) // remove 2
numbers.sort(reverse=True)  # < 10,9,8...
print(numbers[::-1])  # 1, 2, 3...

if 2 in numbers:
    print('2')

print('/' * 50)
for index in range(0, len(numbers)):
    print(f'(posição: {index}, valor: {numbers[index]})')
print('/' * 50)

print('/' * 50)
for index, number in enumerate(numbers):
    print(f'(posição: {index}, valor: {number})')
print('/' * 50)
