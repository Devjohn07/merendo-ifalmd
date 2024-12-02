cartas = ["cavaleiro", "balão", "balao", "mago", "lenhador", "flechas", "mini pekka", "minipekka", "minepeka", "minepekka"]

cartas2 = [ {
    
    "nome": "Mago",
    "Tipo_de_Carta": "terrestre",
    "Raridade": "RARA",
    "Alvos": "terrestre-aéreo",
    "Alcance": "5.5",
    "Velocidade": "média",
          
},

{
    
    "nome": "Cavaleiro",
    "Tipo_de_Carta": "terrestre",
    "Raridade": "COMUM",
    "Alvos": "terrestre",
    "Alcance": "perto",
    "Velocidade": "média",
          
},

{
    
    "nome": "Lenhador",
    "Tipo_de_Carta": "terrestre",
    "Raridade": "LENDÁRIA",
    "Alvos": "terrestre",
    "Alcance": "perto",
    "Velocidade": "muito_rápida",
          
},

{
    
    "nome": "Balão",
    "Tipo_de_Carta": "aérea",
    "Raridade": "ÉPICA",
    "Alvos": "construções",
    "Alcance": "perto",
    "Velocidade": "média",
          
},

{
    
    "nome": "Flechas",
    "Tipo_de_Carta": "Feitiço",
    "Raridade": "COMUM",
    "Alvos": "terrestre-aéreo",
    "Alcance": None,
    "Raio": "1,4",
          
          }
]

resposta = input("Digite o nome da carta que deseja saber as informações, temos as seguintes cartas disponiveis:\n\nCavaleiro\nBalão\nMago\nLenhador\nFlechas\nMini pekka\n\n").lower().strip()

while resposta not in cartas:
    print("Resposta inválida, tente novamente\n")
    resposta = input("Digite a carta desejada: ").lower().strip()

continuar = "sim"
while continuar not in ["nao", "não", "n"] :
    if resposta == "mago":
        print(cartas2[0])

        continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta == "cavaleiro":
        print("\n  nome-----Tipo--Raridade---Alvos-Alcance-Velocidade\n   | \t     |         | \t|     |     |")
        for stat in cavaleiro:
            print(stat["nome"], stat["Tipo_de_Carta"], stat["Raridade"], stat["Alvos"], stat["Alcance"], stat["Velocidade"], sep="/")

        continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta in ["balão", "balao"]:
        print("\n nome--Tipo--Raridade---Alvos-Alcance-Velocidade\n   | \t |    | \t  |     |       |")
        for stat in balao:
            print(stat["nome"], stat["Tipo_de_Carta"], stat["Raridade"], stat["Alvos"], stat["Alcance"], stat["Velocidade"], sep="/")

        continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta == "lenhador":
        print("\n  nome-----Tipo--Raridade---Alvos-Alcance-Velocidade\n   | \t     |         | \t|     |       |")
        for stat in lenhador:
            print(stat["nome"], stat["Tipo_de_Carta"], stat["Raridade"], stat["Alvos"], stat["Alcance"], stat["Velocidade"], sep="/")

        continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta == "flechas":
        print("\nnome-----Tipo-Raridade----Alvos-----Alcance-Velocidade\n | \t   | \t   | \t   | \t       |    |")
        for stat in flechas:
            print(stat["nome"], stat["Tipo_de_Carta"], stat["Raridade"], stat["Alvos"], stat["Alcance"], stat["Raio"], sep="/")
        continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta in  ["mini pekka", "minipekka", "minepekka", "minepeka"]:
        print("\n\tTipo de carta: TROPA TERRESTRE\n\tRaridade: RARA\n\tAlvos: terrestre\n\tAlcance: Perto\n\tVelocidade: rápida\n\n\nEstatisticas que mudam de acordo com o nivel:\n\t\tNIVEL 3\n\n\tPontos de vida: 642\n\tDano: 340\n\tDPS: 212\n\n\t\tNIVEL 15\n\n\tPontos de vida: 1983\n\tDano: 1050\n\tDPS: 656\n")
        continuar = input("Quer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()
