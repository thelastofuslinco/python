import random

machine_number = random.randint(1, 10)
number = -1
c = 0

while number != machine_number:
    number = int(input('Qual o numero de 0 a 10? :'))
    c += 1
    print('Acertou!' if number == machine_number else 'Não!')

print(f'A maquina pensou em {machine_number}.\nVocê jogou {c} vezes para acertar!')
