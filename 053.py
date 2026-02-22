frases = [
    'apos a sopa',
    'a sacada da casa',
    'a torre da derrota',
    'o lobo ama o bolo',
    'anotaram a data da maratona',
    'essa é frase teste'
]

for frase in frases:
    newfrase = ''.join(frase.strip().lower().split())
    reverse_frase = ''.join(frase[::-1].strip().lower().split())

    print(reverse_frase == newfrase)
