#2 formas de imprimir aspas:
"""
USAR ASPAS SIMPLES E DUPLAS;
print ('olá "amigo" ')
OU COM BARRA ANTES DAS ASPAS;
print ("olá /"amigo/" ")
"""

#MÉTODOS DE STRING:
"""
nome = input("fala teu nome:\n")


#deixa em minusculo
print(f"lower\nolá, {nome.lower()}")

#deixa em maiusculo
print(f"upper\n olá, {nome.upper()}")

#converte o primeiro caracter em maiusculo e o restante em minusculo
print(f"capitalize\n olá, {nome.capitalize()}")

#converte o primeiro caracter em maiusculo e o restante em minusculo
print(f"title\n olá, {nome.title()}")

#remove "espaços" a esquerda da entrada
print(f"lstrip\n olá, {nome.lstrip()}")

#remove "espaços" a direita da entrada
print(f"rstrip\n olá, {nome.rstrip()}")

#remove ambos "espaços"
print(f"strip\n olá, {nome.strip()}")

#transforma os elementos da entrada numa "lista"
print(f"split\n olá, {nome.split()}")

#troca uma palavra, letra, frase na string
frase = "hello world"
frase = frase.replace("mundo", nome)

#encontra o indice de uma letra ou palavra na string
input("digite seu nome")
frase = "hello world"
print(frase.find(nome))
"""
#existe vários outros além desses


# forma para usar mais de um metodo na mesma string:
nome = input("fala seu nome e o primeiro sobrenome: ")

nome, sobrenome = nome.split()
nome_completo = nome + " " + sobrenome

print(f"olá, {nome_completo.title()}")