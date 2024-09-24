# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def contar_numeros_por_linha(numero):
    numero_int = int(numero)
    contador = 1
    lista_com_numeros_enviados_por_usuario = []
    contador_para_preencher_lista = 1
    while contador_para_preencher_lista <= numero_int:
        lista_com_numeros_enviados_por_usuario.append(
            contador_para_preencher_lista)
        contador_para_preencher_lista += 1
    while contador <= numero_int:
        print(lista_com_numeros_enviados_por_usuario[:contador])
        contador += 1


numero_inserido = input("Insira um número: ")
contar_numeros_por_linha(numero_inserido)
