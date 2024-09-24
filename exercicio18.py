# Filtrar palavras com mais de 3 letras
# Dada uma lista de palavras, crie uma list comprehension que retorna apenas as palavras com mais de 3 letras.
palavras = ['oi', 'cachorro', 'gato', 'carro', 'a']
palavras_mais_3_letras = [palavra for palavra in palavras if len(palavra) > 3]

print(palavras_mais_3_letras)
