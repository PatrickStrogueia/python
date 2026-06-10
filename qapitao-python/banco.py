"""
PascalCase
snake_case
camelCase
"""

# atributos (self.titular) e argumentos (titular)

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

patrick = ContaBancaria('Patrick', 1000)
maria = ContaBancaria('Maria', 2000)

print(patrick.titular)
print(patrick.saldo)
