from datetime import datetime

from poo.aula_2.classes.Extrato import Extrato


class Conta:
    def __init__(self, numero, saldo, clientes):
        self.numero = numero
        self.saldo = saldo
        self.clientes = clientes
        self.data_inicio = datetime.now()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append([
            'Deposito',
            valor,
            datetime.now()
        ])

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            self.extrato.transacoes.append([
                'saque',
                valor,
                datetime.now()
            ])

            return True
        else:
            print('Saldo insuficiente')
            return False

    def gerar_saldo(self):
        print(f'Conta: {self.numero}, Saldo: {self.saldo}, Clientes: {len(self.clientes)}')

    def transferir(self, conta, valor):
        if self.sacar(valor):
            conta.depositar(valor)
            return f'Valor de {valor} para {conta.numero} transferido com sucesso'
