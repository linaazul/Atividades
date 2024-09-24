# Dobrar os números pares e manter os ímpares
# Escreva uma list comprehension que dobra os números pares e mantém os números ímpares inalterados.
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares_dobrados = [
    n * 2
    # a expressão condicional deve vir antes do for quando você quer aplicar uma operação diferente dependendo de uma condição.
    if n % 2 == 0 else n
    for n in numeros
]


print(numeros_pares_dobrados)
