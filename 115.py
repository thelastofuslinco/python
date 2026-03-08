import json
import os

print(os.getcwd())
ARQUIVO = 'banco.json'


def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def salvar(pessoas):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(pessoas, f, ensure_ascii=False, indent=2)


def listar(pessoas):
    print('-' * 40)
    print(f'{"Listar":^40}')
    print('-' * 40)
    if not pessoas:
        print('Nenhuma pessoa cadastrada.')
        return
    for i, pessoa in enumerate(pessoas, 1):
        print(f'{i}. {pessoa["nome"]} - {pessoa["idade"]} anos')
    print('-' * 40)


def cadastrar(pessoas):
    print('-' * 40)
    print(f'{"Cadastrar":^40}')
    print('-' * 40)

    nome = input('Nome: ').strip()
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('\033[31mIdade inválida! Digite um número.\033[m')

    pessoas.append({'nome': nome, 'idade': idade})
    salvar(pessoas)
    print(f'\033[32m{nome} cadastrado com sucesso!\033[m')


banco = carregar()

print('-' * 40)
print(f'{"Menu principal":^40}')
print('-' * 40)

while True:
    try:
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar uma pessoa')
        print('3 - Sair do sistema')
        print('-' * 40)

        opcao = int(input('Qual a sua opcao? '))

        if opcao < 1 or opcao > 3:
            raise ValueError
        elif opcao == 1:
            listar(banco)
        elif opcao == 2:
            cadastrar(banco)
        elif opcao == 3:
            break
    except (ValueError, TypeError):
        print('\033[31mOpção inválida!\033[m')
