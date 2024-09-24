# Números pares elevados ao cubo
# Escreva uma list comprehension que retorna o cubo dos números pares de uma lista.
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares_ao_cubo = [
    num ** 3
    for num in numeros
    if num % 2 == 0
]

print(numeros_pares_ao_cubo)
