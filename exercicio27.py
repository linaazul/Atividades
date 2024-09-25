# Contar letras em palavras
# Crie um dicionário que conte quantas vezes cada letra aparece em cada palavra de uma lista de palavras. A chave deve ser a palavra, e o valor um dicionário contendo as contagens de letras.

palavras = ['python', 'comprehension', 'dictionary']
letras_por_palavra = {
    palavra: {
        letra: palavra.count(letra)
        for letra in palavra
    }
    for palavra in palavras
}

print(letras_por_palavra)
