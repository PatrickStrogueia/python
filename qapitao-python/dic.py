pessoa = {
    'nome': 'Patrick',
    'idade': 33,
    'cidade': 'Campo Grande',
    'ativo': True
}

print(pessoa)
print(pessoa['nome'])

pessoa['idade'] = 34

pessoa['profissao'] = 'QA'

print(pessoa)

for chave in pessoa:
    print(chave)

for chave, valor in pessoa.items():
    print(f'A chave "{chave}" guarda o valor "{valor}".')
