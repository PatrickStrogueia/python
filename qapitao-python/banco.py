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

patrick = ContaBancaria('Patrick', 1000)
maria = ContaBancaria('Maria', 2000)

print(patrick.titular)
print(patrick.saldo)

patrick.consulta_saldo()
patrick.depositar(500)
patrick.consulta_saldo()
