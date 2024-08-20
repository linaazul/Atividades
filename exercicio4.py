# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def positivo_ou_negativo(numero):
    numero_int = int(numero)
    if numero_int > 0:
        return 'P'
    return 'N'


Positivo = positivo_ou_negativo(10)
negativo = positivo_ou_negativo(-2)
zero = positivo_ou_negativo(0)

print(Positivo)
print(negativo)
print(zero)
