from poo.aula_4.classes.Conta import Conta
from poo.aula_4.classes.Poupanca import Poupanca


class ContaRemuneradaPoupanca(Conta):
    def __init__(self, numero, saldo, clientes, taxa_remuneracao):
        Conta.__init__(self, numero, saldo, clientes)
        Poupanca.__init__(self, taxa_remuneracao)

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30)
