# Multiplicar valores de um dicionário
# Dado um dicionário cujos valores são números inteiros, crie um novo dicionário onde cada valor seja multiplicado por 10.
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
numeros_multiplicados = {
    chave: valor * 10
    for chave, valor in numeros.items()}

print(numeros_multiplicados)
