def maior(*values):
    aux = 0
    for v in values:
        if v > aux:
            aux = v
    print(aux)


maior(4, 10, 28, 1, 4, 5, 16)
