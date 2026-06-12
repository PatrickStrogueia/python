"""
PascalCase
snake_case
camelCase
"""

# atributos (self.titular) e argumentos (titular)

class ContaBancaria:
    
    # construtor
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f'Depósito de R$ {valor} realizado com sucesso!')

    def consulta_saldo(self):
        print(f'Saldo atual de {self.titular}: R$ {self.saldo}.')

# ContaCorrente está herdando as características de ContaBancaria
class ContaCorrente(ContaBancaria):

    def sacar(self, valor):
        taxa = 2
        total = valor + taxa
        if valor > self.saldo:
            print('Saldo insuficiente para saque.')
        else:
            self.saldo = self.saldo - total
            print(f'Saque de R$ {valor} realizado com sucesso. Taxa de R$ {taxa} aplicada.')

# ContaPoupanca está herdando as características de ContaBancaria
class ContaPoupanca(ContaBancaria):

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente para saque.')
        else:
            self.saldo = self.saldo - valor
            print(f'Saque de R$ {valor} realizado com sucesso.')

patrick = ContaCorrente('Patrick', 1000)
maria = ContaPoupanca('Maria', 2000)

print(patrick.titular)
print(patrick.saldo)

patrick.consulta_saldo()
patrick.sacar(500)
patrick.consulta_saldo()
patrick.depositar(100)
patrick.consulta_saldo()

maria.consulta_saldo()
maria.sacar(100)
maria.consulta_saldo()
maria.depositar(200)
maria.consulta_saldo()
