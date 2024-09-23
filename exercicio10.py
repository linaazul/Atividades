# Filtragem de palavras
# Crie uma função que recebe uma lista de palavras e um comprimento mínimo. A função deve retornar uma função(closure) que filtra a lista original, retornando apenas palavras maiores que o comprimento mínimo.

def cria_filtro_de_palavras(numero):
    def filtrar_lista(lista):
        lista_filtrada = []
        for item in lista:
            if len(item) > numero:
                lista_filtrada.append(item)
        return lista_filtrada
    return filtrar_lista


filtro = cria_filtro_de_palavras(5)
# Saída: ['python', 'javascript']
print(filtro(['python', 'java', 'javascript', 'c']))
