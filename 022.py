name = input('Digite o nome: ')

upper = name.upper()
lower = name.lower()
letters = ''.join(name.split())
first_name = name.split()[0]

print('Nome: {}\nUpper: {}\nLower: {}\nLetters: {}\nFist name: {}'.format(name,upper, lower, len(letters), len(first_name)))