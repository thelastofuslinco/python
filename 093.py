jogador = dict()

jogador['nome'] = str(input('Qual o nome do jogador: '))
jogador['partidas'] = []

partidas = int(input('Quantas partidas o jogador: '))
for index in range(partidas):
    jogador['partidas'].append(int(input(f'Quantos gols na partida {index + 1}: ')))

jogador['total'] = sum(jogador['partidas'])
print(jogador)
