import requests

try:
    resposta = requests.get('https://www.google.com')
    print(f'\033[44m{resposta.text}\033[m')
except:
    print('\033[33mErro ao conectar!\033[m')
