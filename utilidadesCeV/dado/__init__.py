def lea_dinheiro(msg):
    while True:
        numero = input(msg).strip().replace(',', '.')
        try:
            valor = float(numero)
            return valor
        except ValueError:
            print('Erro: digite um número válido')
