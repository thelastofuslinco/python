nome = input('Informe o seu nome: ')
nascimento = int(input('Digite o ano de nascimento: '))
ctps = int(input('Digite o numero de sua carteira ou 0 caso nao tenha: '))

usuario = {
    'nome': nome,
    'nascimento': nascimento,
    'carteira': ctps,
}

if usuario['carteira'] != 0:
    usuario['ano_contratacao'] = int(input('Digite o ano de contratação: '))
    usuario['salario'] = float(input('Digite o seu salario: '))
    usuario['aposentadoria'] = usuario['ano_contratacao'] + 35

for key, value in usuario.items():
    print(f'{key}: {value}')
