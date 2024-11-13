# três formas diferentes de input:
"""
nome = input("qual seu nome? ")
print ("bem vindo(a) " + nome)

print ("qual seu nome?")
nome = input()
print = ("Olá, " + nome)

nome = input("qual seu nome? ")
print (f"Olá, {nome}")
"""

"""
#"end" está sendo usado para mudar o sistema padrão do print
e em vez de pular uma linha para printar o "nome", ele simplesmente para na primeira linha
e o que você colocar entre parenteses no "end" vai ser colocado logo após os parenteses da print

EXEMPLO DE "end":
nome = input("qual seu nome?")
print ("olá,", end="")
print(nome)
"""
#"\n" pula uma linha
#"\t" tab
nome = input("digite seu nome:\n")
escola = input("digite o nome de sua escola:\n")
#"f" está sendo usado para "formatar" o texto, alterando o que está entre chaves
print (f"Olá, {nome}, do(a) {escola}. Bem vindo ao nosso sistema!")