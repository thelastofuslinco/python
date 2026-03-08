# modulos e pacotes
from modules.utils import numeros

numero = int(input('Digite um numero: '))
print(f'{numero}! = {numeros.fatorial(numero)}')
print(f'{numero} x 2 = {numeros.dobro(numero)}')
print(f'{numero} x 3 = {numeros.triplo(numero)}')
