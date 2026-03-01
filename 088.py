import random

jogos = list()

total_jogos = int(input('Quantos jogos deseja jogar? '))
j = 0

for i in range(total_jogos):
    jogos.append([])
    print(f'jogo {i + 1}:', end=' ')
    while j <= 6:
        numero = random.randint(1, 10)
        if numero not in jogos[i]:
            jogos[i].append(numero)
            print(numero, end=' ')
            j = j + 1
    j = 0
    print('')
