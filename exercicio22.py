# Filtrar números divisíveis por 3 e 5
# Crie uma list comprehension que retorna apenas os números que são divisíveis por 3 e por 5 de uma lista.

numeros = [10, 15, 30, 22, 18, 45]
numeros_divisiveis = [
    num
    for num in numeros
    if num % 5 == 0 and num % 3 == 0]

print(numeros_divisiveis)
