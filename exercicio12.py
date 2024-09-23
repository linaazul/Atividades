# Função de saudação personalizada
# Crie uma função que retorna uma função personalizada de saudação com base em um nome específico.

def saudacao_para_nome(nome):
    def hora_da_saudacao(hora):
        return f'{hora}, {nome}'
    return hora_da_saudacao


saudar = saudacao_para_nome('Adriel')
print(saudar('Bom dia'))
