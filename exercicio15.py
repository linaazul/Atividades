# Função que cria prefixos para strings
# Crie uma função que recebe um prefixo como argumento e retorna uma função que recebe uma string e retorna essa string com o prefixo anexado.

def cria_prefixo(prefixo):
    def retornar_prefixo_anexado(nome):
        return f'{prefixo} {nome}'
    return retornar_prefixo_anexado


prefixa_com_mr = cria_prefixo('Miss.')
print(prefixa_com_mr('dumbdogs'))
