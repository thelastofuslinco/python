nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Sua nota é {media} Aprovado')
elif media >= 5:
    print(f'Sua nota é {media} Recuperação')
else:
    print(f'Sua nota é {media} Reprovado')
