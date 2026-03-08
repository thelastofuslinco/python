def aumentar(valor=0, porcentagem=100, format=False):
    resultado = valor * (1 + porcentagem / 100)
    if format:
        return moeda(resultado)
    return resultado


def diminuir(valor=0, porcentagem=100, format=False):
    resultado = valor * (1 - porcentagem / 100)

    if format:
        return moeda(resultado)
    return resultado


def dobro(valor=0, format=False):
    resultado = valor * 2

    if format:
        return moeda(resultado)
    return resultado


def metade(valor=0, format=False):
    resultado = valor / 2

    if format:
        return moeda(resultado)
    return resultado


def resumo(preco=0, aumento=0, reducao=0):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do preco: {dobro(preco, format=True)}')
    print(f'Metade do preco: {metade(preco, format=True)}')
    print(f'{aumento}% de aumento: {aumentar(preco, aumento, format=True)}')
    print(f'{reducao}% de redução: {diminuir(preco, reducao, format=True)}')
    print('-' * 30)
    return


def moeda(valor=0):
    return f'R$ {valor:.2f}'.replace('.', ',')
