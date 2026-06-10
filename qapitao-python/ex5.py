print("--- Bem-vindo ao Sistema de Cadastro (v2) ---")

# Todo

cadastro = {}

cadastro["nome"] = input("Qual o seu nome? ")
cadastro["comida"] = input("Qual sua comida favorita? ")
cadastro["cidade"] = input("Onde você mora? ")

print('\n' + '=' * 30)
print("FICHA DE DADOS")
print('=' * 30)

for chave, valor in cadastro.items():
    print(f'{chave.capitalize()}: {valor}')
