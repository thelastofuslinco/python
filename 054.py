from datetime import datetime

years = [
    2008, 1999, 2001, 2002, 2003, 2012, 2010,
]

current_year = datetime.today().year

maior = []
menor = []

for year in years:
    if current_year - year >= 18:
        maior.append(year)
    else:
        menor.append(year)

print(f'{len(maior)} são maiores de 18 anos')
print(f'{len(menor)} são menores de 18 anos')
