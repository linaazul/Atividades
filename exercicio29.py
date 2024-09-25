# Filtrar notas acima de 70
# Dado um dicionário com nomes de alunos e suas notas, crie um novo dicionário que contenha apenas os alunos com notas maiores ou iguais a 70.
notas = {'Alice': 85, 'Bob': 67, 'Charlie': 90, 'Dave': 45}
notas_altas = {
    aluno: nota
    for aluno, nota in notas.items()
    if nota >= 70
}

print(notas_altas)
