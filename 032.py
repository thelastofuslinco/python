year = int(input('Digite o ano: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Ano é bissexto")
else:
    print('Ano nao é bissexto')
