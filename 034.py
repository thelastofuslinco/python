salario = float(input('Qual o seu salario: '))

if salario <= 1250:
    print(f'O aumento é de {salario * 1.15:.2f}')
else:
    print(f'O aumento é de {salario * 1.10:.2f}')
