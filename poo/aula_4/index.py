from classes.Cliente import Client
from classes.Conta import Conta
from poo.aula_4.classes.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca

client1 = Client('Lincoln', '000.000.000-00', 'Avenida x')
client2 = Client('Maria', '000.000.000-00', 'Avenida y')

conta1 = Conta(1, 100, [client1, client2])
conta2 = Conta(2, 100, [client1, client2])
conta3 = ContaRemuneradaPoupanca(3, 100, [client1, client2], 0.1)

conta1.depositar(250)
conta1.sacar(100)
conta1.sacar(100000)
conta1.transferir(conta2, 5)

conta1.extrato.gerar_extrato(conta1.numero)
conta1.gerar_saldo()

conta3.remuneraConta()
conta3.gerar_saldo()
