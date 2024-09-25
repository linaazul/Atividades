# Temperaturas em Celsius para Fahrenheit:
# Crie uma lista de temperaturas em Celsius e use dictionary comprehension para criar um dicionário onde as chaves são as temperaturas em Celsius e os valores são as temperaturas convertidas para Fahrenheit.

celsius = [0, 20, 37, 100]
fahrenheit = {temp: (temp * 9/5) + 32 for temp in celsius}

print(fahrenheit)
