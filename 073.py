times = ('palmeiras', 'são paulo', 'fluminense', 'bahia', 'corinthians',
         'atletico-pr', 'bragantino', 'chapecoense', 'mirasol', 'coritiba',
         'flamengo', 'botafogo', 'gremio', 'ec vitoria', 'atletico-mg', 'remo',
         'vasco da gama', 'santos', 'internacional', 'cruzeiro')

print('Os cinco primeiros são:\n')

for index in range(0, 5):
    print(times[index])

print('Os 4 ultimos colocados são:\n')

for time in times[len(times) - 4:]:
    print(time)

print(f'Times em ordem alphabetica: {sorted(times)}')

print(f'O time chapecoense esta na posição {times.index("chapecoense") + 1}')
