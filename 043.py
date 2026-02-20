weight = float(input('Qual o valor do seu peso em kg: '))
height = float(input('Qual a sua altura em metros: '))

imc = weight / (height ** 2)

print(f'{imc:.2f} ')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('obesidade morbida')
