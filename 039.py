from datetime import datetime

year = int(input('Digite o ano de nascimento: '))
age = datetime.today().year - year

if age == 18:
    print('Esta na hora de se alistar!')
elif age > 18:
    print(f'passou do prazo de alistar! prazo: {age - 18}')
else:
    print(f'Ainda nao esta na hora de se alistar faltam {18 - age} anos')
