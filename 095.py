jogadores = list()

while True:
    jogador = dict()
    jogador['nome'] = str(input('Qual o nome do jogador: '))
    jogador['partidas'] = []

    partidas = int(input('Quantas partidas o jogador: '))
    for index in range(partidas):
        jogador['partidas'].append(int(input(f'Quantos gols na partida {index + 1}: ')))

    jogador['total'] = sum(jogador['partidas'])
    jogadores.append(jogador)

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 20)

print(f'{"ID":<5} {"Nome":<15} {"Partidas":<10} {"Gols":<10}')
print('-' * 45)
for index, value in enumerate(jogadores):
    print(f'{index:<5} {value["nome"]:<15} {len(value["partidas"]):<10} {value["total"]:<10}')
print('-=' * 20)

while True:
    id_jogador = int(input('Mostrar dados de qual jogador? (999 para parar): '))

    if id_jogador == 999:
        break

    if id_jogador < 0 or id_jogador >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {id_jogador}!')
    else:
        j = jogadores[id_jogador]
        print(f'-- LEVANTAMENTO DO JOGADOR {j["nome"]}:')
        for i, g in enumerate(j['partidas']):
            print(f'   No jogo {i + 1} fez {g} gols.')
    print('-' * 45)
