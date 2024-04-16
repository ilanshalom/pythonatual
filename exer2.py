
medias = []


for i in range(4):
    notas = []

    for j in range(1):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)
    media = sum(notas) / 4
    medias.append(media)


alunos_aprovados = sum(1 for media in medias if media >= 7.0)
alunos_reprovados = sum(1 for media in medias if media <= 7.0)


print("Número de alunos com média maior ou igual a 7.0:", alunos_aprovados)
print("Número de alunos com média menor a  7.0:", alunos_reprovados)
