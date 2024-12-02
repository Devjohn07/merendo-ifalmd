def main():
    numeros = input("digite os valores como no exemplo a seguir(10 + 5) --> ").split()
    calc(numeros[0], numeros[1], numeros[2])

def calc(num1, operador, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operador == "-":
        print(num1 - num2)
    
    if operador == "+":
        print(num1 + num2)
    
    if operador == "/":
        print(num1 / num2)
    
    if operador == "*":
        print(num1 * num2)
    
    if operador == "**":
        print(num1 - num2)

    else:
        print("Operador não identificado")

main()
