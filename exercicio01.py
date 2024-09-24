# Faça um programa para imprimir:
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimir_numero(numero):
    contador = 1
    numero_int = int(numero)
    while contador <= numero_int:
        contador_str = str(contador)
        print(f"{(contador_str + ' ') * (contador)}")
        contador += 1


teste = input("Escreva um numero: ")
imprimir_numero(teste)
