def main():
    num = int(input("Qual será o tamanho do bloco?\n"))
    bloco(num)

def bloco(num):
    bloco = ("⬜" * num)
    print(f"{bloco}\n" * num, end="")


main()
