# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# Variável para encerrar o laço.
encerrar = None
# Lista com as tarefas descritas pelo usuário
lista_de_tarefas = []
# Lista com as tarefas que o usuário decidiu apagar
tarefas_descartadas = []

# Laço while
while encerrar != True:
    # Print na linha 19 e 23 para deixar mais visualmente legível
    print()
    print('Comandos: listar, desfazer, refazer, encerrar.')
    comando_ou_tarefa = input('Digite uma tarefa ou comando: ')
    print()

    def listar(lista):
        # Checa se a lista está vazia, caso esteja nada vai ser listado
        if len(lista) != 0:
            print()
            print("TAREFAS:")
            # Caso a lista nao esteja vazia, usei o join para mostrar item por item na lista
            return "\n".join(item for item in lista)
        return "Nada para listar ainda."

    def desfazer(lista_tarefas, lista_descartados):
        # Checa se a lista está vazia, caso esteja nada é desfeito
        if len(lista_tarefas) == 0:
            return "Nada a desfazer."
        # Variável para armazenar o último item da lista de tarefas
        item_descartado = lista_tarefas[-1]
        # Na lista de itens descartados entra o último item da lista de tarefas
        lista_descartados.append(item_descartado)
        # Último item da lista de tarefas é apagado
        lista_tarefas.pop()
        return listar(lista_tarefas)

    def refazer(lista_descartados, lista_tarefas):
        # Checa se a lista está vazia, caso esteja nada é refeito
        if len(lista_descartados) == 0:
            return "Nada a ser refeito."
        # Variável para armazenar o último item da lista de tarefas descartadas
        item_descartado = lista_descartados[-1]
        # Último item da lista de tarefas descartadas é apagado
        lista_descartados.pop()
        # Último item da lista de tarefas descartdas é adicionado a lista de tarefas
        lista_tarefas.append(item_descartado)
        return listar(lista_tarefas)

    if comando_ou_tarefa == 'listar':
        teste = listar(lista_de_tarefas)
        print(teste)
    elif comando_ou_tarefa == 'desfazer':
        desfazendo = desfazer(lista_de_tarefas, tarefas_descartadas)
        print(desfazendo)
    elif comando_ou_tarefa == 'refazer':
        refazendo = refazer(tarefas_descartadas, lista_de_tarefas)
        print(refazendo)
    elif comando_ou_tarefa == 'encerrar':
        encerrar = True
        continue
    else:
        lista_de_tarefas.append(comando_ou_tarefa)
