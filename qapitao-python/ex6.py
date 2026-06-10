# Todo

def calcular_total(valor_produto, peso_kg):
    valor_do_frete = peso_kg * 10
    total = valor_produto + valor_do_frete
    return total
    
print('--- Sistema de Logística ---')

v_prod = float(input('Qual o valor do produto? R$ '))
peso = float(input('Qual o peso (Kg)? '))

valor_final = calcular_total(v_prod, peso)

print(f'O valor total com frete é: R$ {valor_final}')
