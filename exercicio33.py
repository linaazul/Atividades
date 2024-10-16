# Implemente uma função chamada score_points que recebe uma lista de números inteiros representando pontuações e retorna uma nova lista onde cada elemento é a posição (pontuação relativa) do número correspondente na lista original, baseada na ordem decrescente dos valores únicos.

def score_points(lista_com_pontos):
    set_lista = set(lista_com_pontos)
    lista_invertida =sorted(set_lista, reverse=True)
    final_score = []
    for numero_lista_original in lista_com_pontos:
        for index, numero_lista_invertida in enumerate(lista_invertida, start=1):
            if numero_lista_invertida == numero_lista_original:
                final_score.append(index)
    return final_score

teste = score_points([9,4,3,10])
teste_2 = score_points([2, 2, 20, 5, 1, 70])
print(teste)
print(teste_2)
