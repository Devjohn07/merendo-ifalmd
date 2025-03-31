alunos = ["Hermione", "Harry", "Rony"]
professores = ["Bob Esponja", "Lula Molusco", "Patrick Estrela", "Sirigueijo"]

def main():
    yon = input("Escolha uma das seguintes listas:\n\nAlunos\nProfessores")
    if listas(yon) == True:
        print("\nAlunos: \n")
        for i in range(len(alunos)):
            print(i + 1, professores[i], "\n")
    else:
        print("Professores: \n")
        for i in range(len(professores)):
            print(i + 1, professores[i], "\n")

            
#A função "len" retorna a quantidade de itens na lista
def listas(yon):
    if yon == "Alunos":
        return True
    elif yon == "Professores":
        return False


