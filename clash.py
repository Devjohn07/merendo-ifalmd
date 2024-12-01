resposta = input("Digite o nome da carta que deseja saber as informações, temos as seguintes cartas disponiveis:\n\nCavaleiro\nBalão\nMago\nLenhador\nFlechas\nMini pekka\n\n").lower().strip()

while resposta not in ["cavaleiro", "balão", "balao", "mago", "lenhador", "flechas", "mini pekka", "minipekka"]:
    print("Resposta inválida, tente novamente\n")
    resposta = input("Digite a carta desejada: ").lower().strip()

continuar = "sim"
while continuar not in ["nao", "não", "n"] :
    if resposta == "mago":
        print("\n\tTipo de carta: TROPA TERRESTRE\n\tRaridade: RARA\n\tAlvos: terrestre/aéreo\n\tAlcance: 5.5\n\tVelocidade: média\n\n\nEstatisticas que mudam de acordo com o nivel:\n\t\tNIVEL 3\n\n\tPontos de vida: 356\n\tDano: 133\n\tDPS: 95\n\n\t\tNIVEL 15\n\n\tPontos de vida: 1100\n\tDano: 410\n\tDPS: 292\n")
        continuar = input("Quer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta == "cavaleiro":
        print("\n\tTipo de carta: TROPA TERRESTRE\n\tRaridade: COMUM\n\tAlvos: terrestre\n\tAlcance: Perto\n\tVelocidade: média\n\n\nEstatisticas que mudam de acordo com o nivel:\n\t\tNIVEL 1\n\n\tPontos de vida: 690\n\tDano: 79\n\tDPS: 65\n\n\t\tNIVEL 15\n\n\tPontos de vida: 2560\n\tDano: 293\n\tDPS: 244\n")
        continuar = input("Quer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta in ["balão", "balao"]:
        print("\n\tTipo de carta: TROPA AÉREA\n\tRaridade: ÉPICA\n\tAlvos: construções\n\tAlcance: Perto\n\tVelocidade: média\n\n\nEstatisticas que mudam de acordo com o nivel:\n\t\tNIVEL 6\n\n\tPontos de vida: 1050\n\tDano: 400\n\tDPS: 200\n\tDano de morte: 150\n\n\t\tNIVEL 15\n\n\tPontos de vida: 2446\n\tDano: 932\n\tDPS: 466\n\tDano de morte: 349\n")
        continuar = input("Quer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta == "lenhador":
        print("\n\tTipo de carta: TROPA TERRESTRE\n\tRaridade: LENDÁRIA\n\tAlvos: terrestre\n\tAlcance: Perto\n\tVelocidade: muito rápida\n\n\nEstatisticas que mudam de acordo com o nivel:\n\t\tNIVEL 9\n\n\tPontos de vida: 1060\n\tDano: 200\n\tDPS: 250\n\n\t\tNIVEL 15\n\n\tPontos de vida: 1865\n\tDano: 352\n\tDPS: 440\n")
        continuar = input("Quer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta == "flechas":
        print("\n\tTipo de carta: FEITIÇO\n\tRaridade: COMUM\n\tAlvos: terrestre/aéreo\n\tRaio: 1,4\n\n\nEstatisticas que mudam de acordo com o nivel:\n\t\tNIVEL 1\n\n\tDano: 144\n\tDano na torre: 36\n\n\t\tNIVEL 15\n\n\tDano: 534\n\tDano na torre: 135\n")
        continuar = input("Quer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()

    if resposta in  ["mini pekka", "minipekka"]:
        print("\n\tTipo de carta: TROPA TERRESTRE\n\tRaridade: RARA\n\tAlvos: terrestre\n\tAlcance: Perto\n\tVelocidade: rápida\n\n\nEstatisticas que mudam de acordo com o nivel:\n\t\tNIVEL 3\n\n\tPontos de vida: 642\n\tDano: 340\n\tDPS: 212\n\n\t\tNIVEL 15\n\n\tPontos de vida: 1983\n\tDano: 1050\n\tDPS: 656\n")
        continuar = input("Quer ver as informações de outra carta? ").lower().strip()
        if continuar in ["sim", "s"]:
            resposta = input("Digite a carta desejada: ").lower().strip()
        elif continuar in ["nao", "n"]:
            break
        else:
            print("Comando não identificado, tente novamente:\n")
            resposta = input("Digite a carta desejada: ").lower().strip()
