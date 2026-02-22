weights = [
    100,
    50,
    45,
    23,
    150
]

max = weights[0]
min = weights[0]

for weight in weights:

    if weight > max:
        max = weight
    if weight < min:
        min = weight
print(f'Peso maximo de {max} e menor de {min}')
