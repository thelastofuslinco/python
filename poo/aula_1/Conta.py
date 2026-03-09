class Conta:
    def __init__(self, numero, saldo, nome, cpf):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.cpf = cpf

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            return True
        else:
            print('Saldo insuficiente')
            return False

    def extrato(self):
        print(f'numero: {self.numero}, saldo: {self.saldo}, nome: {self.nome}, cpf: {self.cpf}')

    def transferir(self, conta, valor):
        if self.sacar(valor):
            conta.depositar(valor)
            return f'Valor de {valor} para {conta.numero} transferido com sucesso'


# exemplo
conta1 = Conta(1, 100, 'Joao', '000.000.000-00')
conta2 = Conta(2, 200, 'Maria', '000.000.000-00')

print(conta1.transferir(conta2, 50))

conta1.extrato()
conta2.extrato()
