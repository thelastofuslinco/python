# help
help(print)


# docstrings
def contador(x, y, z):
    """
    Função contador de um numero x ate y contado em z
    :param x: inicio da contagem
    :param y: fim da contagem
    :param passo: Passo da contagem
    :return: nulo
    """
    if z == 0:
        z = 1

    print(f'De {x} até {y} contando em {z}')

    if x > y and z > 0 or x < y and z < 0:
        z = -z

    for c in range(x, y, z):
        print(c, end=' ')
    print('')


help(contador)


# parametro opcional
def somar(a=0, b=0, c=0):
    """
    Soma valores de um numero a ser somado
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: Soma de todos os valores da primeira linha
    """
    return a + b + c


# Escopo de variaveis
def escopo(b):
    global d
    a = 10
    b += 4
    c = 2
    d = 3
    print(f'O valor de a dentro do esoopo vale {a}')
    print(f'O valor de b dentro do esoopo vale {b}')
    print(f'O valor de c dentro do esoopo vale {c}')
    print(f'O valor de d dentro do esoopo vale {d}')
    return


a = 5
d = 2
escopo(a)
print('-' * 40)
print(f'O valor de a fora do escopo é {a}')
print(f'O valor de d fora do escopo é {d}')
print('-' * 40)


# Retorno de valores
def fatorial(n=1):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


n = 5
print(f'Fatorial de {n}! = {fatorial(n)}')
print(f'Fatorial de 1! = {fatorial()}')


def isPare(num):
    if num % 2 == 0:
        return True
    else:
        return False


numero = 2

if isPare(numero):
    print(f'Numero {numero} é par')
else:
    print(f'Numero {numero} é impar')
