# Gerador de multiplicadores
# Crie uma função cria_multiplicador que recebe um número e retorna uma função que multiplica qualquer número por aquele número inicial.

def criar_multiplicador(numero):
    def multiplicar(numero_2):
        return numero * numero_2
    return multiplicar


multiplicar_por_4 = criar_multiplicador(4)
print(multiplicar_por_4(10))
