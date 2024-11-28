def main():
    calc = input("Digite a operação (ex: 5 + 3): ").strip()
    calculo(calc)

"""
"eval" é uma função que pega uma string e lê ela como se não fosse uma string
Por exemplo, se eu tiver a string: "10 + 4" em vez dele ler ela como uma string,
ele vai ler ela como literalmente 10 + 4
"""

def calculo(numeros):
    resultado = eval(numeros)
    if resultado == eval(numeros):
      print(f"Resultado: {resultado}")
    else:
        print("Erro: Entrada inválida. Use números e operadores válidos (+, -, *, /).")

main()