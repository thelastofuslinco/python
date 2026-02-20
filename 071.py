saque = int(input('Digite o valor do saque: '))
notas = [50, 20, 10, 1]
cedulas = []

while saque > 0:
    for nota in notas:
        if saque >= nota:
            saque -= nota
            cedulas.append(nota)
            break

for nota in set(cedulas):
    quantidade = cedulas.count(nota)

    if quantidade > 0:
        print(f'{quantidade}x R$ {nota}')
