# def mostrar_nome(nome):
#     print(nome)

# mostrar_nome('Patrick')

# print('Strogueia')

# def converter_para_real(valor_em_dolar):
#     cotacao = 5.50
#     resultado = valor_em_dolar * cotacao
#     return resultado

# valor_convertido = converter_para_real(100)

# print(valor_convertido)

def criar_email_corporativo(nome: str, empresa: str):
    email = f'{nome}@{empresa}.com'
    return email.lower()

email_patrick = criar_email_corporativo('Patrick', 'TIVIT')
email_strogueia = criar_email_corporativo('Strogueia', 'Google')
email_maria = criar_email_corporativo('Maria', 'Tesla')

print(email_patrick, email_strogueia, email_maria)
