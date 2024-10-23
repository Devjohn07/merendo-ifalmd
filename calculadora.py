# Menu da calculadora
print ("---------------------------------------------------------------------------------------------------------------------------")
print("\t \t \t \t \t \t CALCULADORA TEXTUAL")
print ("---------------------------------------------------------------------------------------------------------------------------")
print("\n")
operacao = input("digite qual operação deseja usar(digite exatamente como ilustrado a seguir): \nsoma: + \nsubtração: - \nmultiplicação: * \ndivisão: /\nelevado a: **\n \n")
print ("\n")

#
if operacao not in ["+", "-", "*", "/", "**"]:
    print("---------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t OPERAÇÃO INVALIDA, TENTE NOVAMENTE!")
    print("---------------------------------------------------------------------------------------------------------------------------")

#solicita os valores    
else:
     x = int (input("Ok, digite o primeiro numero da operação: ")) 
     y = int(input("o segundo numero: "))
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
     if operacao == "**":
        print("PERFEITO, seu calculo está aqui:\n")
        print(f"{x} ** {y} = {x ** y}")
