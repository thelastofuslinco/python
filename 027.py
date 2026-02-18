name = input('Digite seu nome: ')

first_name = name.split()[0]
last_name = name.split()[-1]

print('O nome é {}\nO primeiro nome é {}\n O ultimo nome é {}'.format(name, first_name, last_name))
