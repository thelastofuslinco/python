frase = input('Digite uma frase: ')

times_a = frase.upper().count('A')
first_index = frase.upper().find('A')
last_index = frase.upper().rfind('A')

print('Frase é {}, tem A {}X, o primeiro indice é {}, o ultimo indice é {}'.format(frase, times_a, first_index,
                                                                                   last_index))
