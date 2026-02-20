import random

number = int(input('Digite um numero:'))

machine_number = random.randint(1, 5)

print(f'A maquina pensou em {machine_number} seu numero é {number}')
print('Venceu!' if number == machine_number else 'Perdeu!')
