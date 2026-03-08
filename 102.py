def fatorial(n, show=False):
    f = 1
    for i in range(1, n + 1):
        f *= i
        if show:
            print(f'{f} x', end=' ')

    if show:
        print('=', end=' ')
    return f


print(f'{fatorial(5)}')
print(f'{fatorial(5, True)}')
