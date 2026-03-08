def notas(*valores, sit=False):
    """
    :param valores: Total de notas de todos os alunos
    :return: dicionario com notas de todos os alunos
    """
    alunos = {}
    media = sum(valores) / len(valores)

    if media < 6 and sit:
        alunos['situacao'] = 'Ruim'
    elif (media >= 6) and sit:
        alunos['situacao'] = 'Boa'

    alunos.update({
        'media': media,
        'menor': min(valores),
        'maior': max(valores),
        'quantidade': len(valores),
    })
    return alunos


print(notas(9, 8, 5, 10, sit=True))
print(notas(9, 6, 5, 2, sit=True))
