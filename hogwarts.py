alunos = ["Hermione", "Harry", "Rony"]
professores = ["Bob Esponja", "Lula Molusco", "Patrick Estrela", "Sirigueijo"]

#A função "len" retorna a quantidade de itens na lista
print("Professores: \n")
for i in range(len(professores)):
    print(f"{i + 1} {professores[i]}\n")

print("\nAlunos: \n")
for i in range(len(alunos)):
    print(f"{i + 1} {professores[i]}\n")