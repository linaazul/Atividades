# Filtrar e converter para maiúsculas
# Dada uma lista de strings, crie uma list comprehension que filtra apenas as strings que começam com a letra "a" e as converte para maiúsculas.
fruits = ['apple', 'banana', 'avocado', 'grape']
fruits_with_a = [
    fruta.upper()
    for fruta in fruits
    if fruta[0] == 'a'
]

print(fruits_with_a)
