# Gerador de contadores
# Crie uma função que retorna uma função(closure) que incrementa um valor em cada chamada. A função principal deve receber um valor inicial como parâmetro e retornar uma função que, quando chamada, incrementa o valor inicial.
def cria_contador(numero):
    def adiciona_um():
        nonlocal numero
        numero += 1
        return numero
    return adiciona_um


contador = cria_contador(5)
print(contador())  # Saída: 6
print(contador())  # Saída: 7
