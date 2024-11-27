#Essa funçã recebe e envia dados para o usuário
def main():
    rai = float(input("qual é o raio? "))
    cal(rai)
    print(f"A área do circulo de raio {rai} é: {area}")

#calcula o raio e muda para o metodo brasileiro
def cal(raio):
    global area
    area = f"{(3.141516 * raio**2):_.2f}"
    area = area.replace(".", ",")
    area = area.replace("_", ".")


main()