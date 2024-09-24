# Filtrar dicionários por valor
# Dada uma lista de dicionários com nomes e idades, filtre apenas os dicionários onde a idade é maior que 18.
pessoas = [
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Pedro', 'idade': 17},
    {'nome': 'Maria', 'idade': 20}
]

maiores_de_idade = [
    pessoa
    for pessoa in pessoas
    if pessoa['idade'] >= 18
]

print(maiores_de_idade)
