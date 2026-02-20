valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salario: '))
anos_pagar = int(input('Quantos anos de pagamento: '))

prestacao = valor_casa / (anos_pagar * 12)
is_aprovado = prestacao <= salario * 0.30

if is_aprovado:
    print("aprovado")
else:
    print("reprovado")
