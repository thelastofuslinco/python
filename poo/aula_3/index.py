class Conta:
    __total_contas = 0

    @classmethod
    def total_contas(cls):
        return cls.__total_contas

    def __init__(self, n, s):
        self.__numero = n
        self.__saldo = s

        type(self).__total_contas += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print('Valor invalido')
        else:
            self.__saldo = valor

    def gerar_saldo(self):
        print(f'O saldo da conta {self.__numero}: {self.__saldo}')

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor


# exemplo
conta1 = Conta(1, 1000)
conta2 = Conta(2, 100)

conta1.sacar(10000)

conta1.saldo = -10000
print(conta1.saldo)

conta1.gerar_saldo()
conta2.gerar_saldo()

print(f'Total de contas: {Conta.total_contas()}')
