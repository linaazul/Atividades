# Lista de listas filtrando números pares
# Dada uma lista de listas de números, crie uma list comprehension que retorna apenas os números pares de todas as sublistas.
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numeros_pares = [
    num
    for lista in listas
    for num in lista
    if num % 2 == 0
]

print(numeros_pares)
