def main():
    num = int(input("Qual o tamanho desejado da linha? "))
    tamanho(num)

def tamanho(num):
    print("⬜" * num, end="")

main()