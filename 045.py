import random

player = input('Digite tesoura | pedra | papel: ').strip().lower()
machine = random.randint(0, 2)

rules = {
    0: 'pedra',
    1: 'papel',
    2: 'tesoura',
}

print(f'jogador jogou {player}')
print(f'maquina jogou {rules[machine]}')

if player == rules[machine]:
    print('empate')
elif player == 'pedra':
    if rules[machine] == 'papel':
        print('jogador perdeu')
    else:
        print('jogador ganhou')
elif player == 'papel':
    if rules[machine] == 'tesoura':
        print('jogador perdeu')
    else:
        print('jogador ganhou')
else:
    if rules[machine] == 'pedra':
        print('jogador perdeu')
    else:
        print('jogador ganhou')
