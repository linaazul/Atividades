# Quadrado dos números ímpares
# Crie uma list comprehension que retorna o quadrado dos números ímpares de uma lista.
numeros = [1, 2, 3, 4, 5, 6, 7]
numeros_impares = [n ** 2 for n in numeros if n % 2 != 0]

print(numeros_impares)
