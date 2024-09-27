# Receber uma lista de palavras e checar se elas possuem as mesmas letras
# exemplo: bac, cab == palavras identicas

def quantas_palavras_identicas(lista_de_palavras):
    palavras_identicas = 0
    # para formar os pares é necessario duas variaveis.
    # Uma externa que vai percorrer até o penúltimo item da lista
    # E uma interna pra fazer a combinacao da externa com a interna

    # Aqui é necessário o -1 pois no último indice não tem mais como formar par
    for indice_externo in range(len(lista_de_palavras) - 1):
        # Nesse caso eu nao posso ter o par com a mesma string
        # Então é necessário somar mais um a variavel externa para que seja diferente da interna
        for indice_interno in range(indice_externo + 1, len(lista_de_palavras)):
            # O set faz com que as palavras tenham letras únicas, assim é mais facil de comparar
            if set(lista_de_palavras[indice_externo]) == set(lista_de_palavras[indice_interno]):
                palavras_identicas += 1
    return palavras_identicas


strings_identicas = ["good", "god", "yarn", "bac", "aabc"]
print(quantas_palavras_identicas(strings_identicas))
