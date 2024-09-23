# Simulação de desconto progressivo
# Crie uma função chamada desconto_progressivo que retorna uma função capaz de aplicar um desconto cumulativo em uma série de valores. Cada vez que a função interna for chamada, o valor do desconto aumenta.

def desconto_progressivo(desconto):
    desconto_progressivo = 0

    def aplica_desconto(valor):
        nonlocal desconto_progressivo
        desconto_progressivo += desconto
        resultado = valor - (desconto_progressivo/100 * valor)
        if resultado == 0:
            raise Exception(
                "O valor já é 0, então não é mais necessário desconto")
        return int(resultado)
    return aplica_desconto


descontar = desconto_progressivo(5)
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
print(descontar(100))
