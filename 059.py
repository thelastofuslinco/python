numbers = [
    int(input('Digite um numero inteiro: ')),
    int(input('Digite outro numero inteiro: ')),
]

while True:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair')

    opcao = int(input('Qual sua opcao: '))

    if opcao == 1:
        soma = numbers[0] + numbers[1]
        print(f'A soma entre {numbers[0]} e {numbers[1]} é {soma}')
    elif opcao == 2:
        multiplicar = numbers[0] * numbers[1]
        print(f'A multiplicação de {numbers[0]} e {numbers[1]} é {multiplicar}')
    elif opcao == 3:
        maior = max(numbers[0], numbers[1])

        print(f'O maior numero é {maior}')
    elif opcao == 4:
        numbers = [
            int(input('Digite um numero inteiro: ')),
            int(input('Digite outro numero inteiro: ')),
        ]
    elif opcao == 5:
        break
    else:
        print('Opção invalida')
