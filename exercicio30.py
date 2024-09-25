# Inverter chaves e valores de um dicionário
# Dado um dicionário, crie um novo dicionário invertendo as chaves e os valores.
dicionario = {'maçã': 1, 'banana': 2, 'laranja': 3}
valores_invertidos = {
    valor: chave
    for chave, valor in dicionario.items()
}

print(valores_invertidos)
