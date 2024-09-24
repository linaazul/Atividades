# Somar os elementos de duas listas
# Dadas duas listas de números de mesmo comprimento, crie uma list comprehension que retorna uma nova lista com a soma dos elementos nas mesmas posições.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

listas_somadas = [num1 + num2 for num1, num2 in zip(lista1, lista2)]

print(listas_somadas)
