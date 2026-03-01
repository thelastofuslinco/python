alunos = [
    ['Lincoln', [5, 7]],
    ['Joao', [7, 7]],
    ['Maria', [10, 8]]
]

while True:
    alunos.append([
        input('Digite o nome do aluno: '),
        [int(number.strip()) for number in input('Digite um numero com ",": ').split(',')],
    ])

    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar in 'Nn':
        break

print(f"{'Nº':<5} {'Nome':<10} {'Média':<8}")
print("-" * 35)

for index, aluno in enumerate(alunos):
    nome = aluno[0]
    media = sum(aluno[1]) / len(aluno[1])
    print(f"{index:<5} {nome:<10} {media:<8.1f}")

while True:
    index = int(input('Digite o indentificador de cada aluno ou 999 para sair: '))

    if index == 999:
        break
    print(f'Aluno {alunos[index][0]} tirou {alunos[index][1]}')
