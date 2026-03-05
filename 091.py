import random
from operator import itemgetter

my_dict = {
    'Jogador 1': random.randint(1, 6),
    'Jogador 2': random.randint(1, 6),
    'Jogador 3': random.randint(1, 6),
    'Jogador 4': random.randint(1, 6),
}
print('Jogo ')
for key, value in my_dict.items():
    print(f'{key} tirou {value}')
print()
print('Ranking')
sorted_dict = enumerate(sorted(my_dict.items(), key=itemgetter(1), reverse=True))

for key, value in sorted_dict:
    print(f'{key + 1}° {value[0]}: {value[1]}')
