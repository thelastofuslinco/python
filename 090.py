nome = input('Qual o seu nome? ')
media = float(input("Qual foi a sua media? "))

aluno = {
    'nome': nome,
    'media': media,
    'situação': media >= 6 and 'Aprovado' or 'Reprovado',
}

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
