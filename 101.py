def voto(ano):
    from datetime import date
    age = date.today().year - ano

    print(f'Com {age} anos de idade')

    if age < 16:
        return 'NEGADO'
    elif 16 <= age < 18 or age > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATORIO'


ano = int(input('Digite seu ano de nascimento: '))
print(f'Seu voto é {voto(ano)}')
