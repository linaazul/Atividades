# Calculadora personalizada
# Crie uma função chamada cria_calculadora que retorna uma função de operação aritmética com base em uma string que define a operação('soma', 'subtrai', 'multiplica', ou 'divide').
def cria_calculadora(operacao_string):
    def soma(numero_1, numero_2):
        return numero_1 + numero_2

    def subtrai(numero_1, numero_2):
        return numero_1 - numero_2

    def multiplica(numero_1, numero_2):
        return numero_1 * numero_2

    def dividir(numero_1, numero_2):
        return numero_1 / numero_2

    if operacao_string == 'soma':
        return soma
    elif operacao_string == 'subtrai':
        return subtrai
    elif operacao_string == 'multiplica':
        return multiplica
    else:
        return dividir


soma = cria_calculadora('soma')
print(soma(3, 4))  # Saída: 7

multiplica = cria_calculadora('multiplica')
print(multiplica(3, 4))  # Saída: 12
