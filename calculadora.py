
print ("---------------------------------------------------------------------------------------------------------------------------")
print("\t \t \t \t \t \t CALCULADORA TEXTUAL")
print ("---------------------------------------------------------------------------------------------------------------------------")
print("\n")
operacao = input("digite qual operação deseja usar(digite exatamente como mostrado a seguir): \n + \n - \n * \n /\n \n")
print ("\n")
x = int (input("Ok, digite o primeiro numero da operação: ")) 
y = int(input("o segundo numero: "))
print("\n")

if operacao == "+":
    print("PERFEITO, seu calculo está aqui:\n")
    print(f"{x} + {y} = {x + y}")

if operacao == "-":
    print("PERFEITO, seu calculo está aqui:\n")
    print(f"{x} - {y} = {x - y}")

if operacao == "*":
    print("PERFEITO, seu calculo está aqui:\n")
    print(f"{x} * {y} = {x * y}")

if operacao == "/":
    print("PERFEITO, seu calculo está aqui:\n")
    print(f"{x} / {y} = {x / y}")





