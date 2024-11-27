#Versão mais simplificada de "paridade2"

#ENTRADA: pede os valores
def main():
    num = int(input("Digite um número e direi se ele é par ou impar: "))
    if verificacao(num):
        print("É par")
    else:
        print("É impar")
        
#PROCESSAMENTO: verifica a paridade
def verificacao(num):
    return num % 2 == 0

#SAIDA: executa o programa
main()