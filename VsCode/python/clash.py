cartas2 = [ {
    
    "nome": "Mago",
    "Tipo_de_Carta": "terrestre",
    "Raridade": "RARA",
    "Alvos": "terrestre-aéreo",
    "Alcance": "5.5",
    "Velocidade": "média",
    "Pontos de vida1": "356",
    "Dano1": "133",
    "dps1": "95",
    "Pontos de vida2": "1.100",
    "Dano2": "410",
    "dps2": "292"
},

{
    
    "nome": "Cavaleiro",
    "Tipo_de_Carta": "terrestre",
    "Raridade": "COMUM",
    "Alvos": "terrestre",
    "Alcance": "perto",
    "Velocidade": "média",
    "Pontos de vida1": "690",
    "Dano1": "79",
    "dps1": "65",
    "Pontos de vida2": "2.566",
    "Dano2": "293",
    "dps2": "244"
},

{
    
    "nome": "Lenhador",
    "Tipo_de_Carta": "terrestre",
    "Raridade": "LENDÁRIA",
    "Alvos": "terrestre",
    "Alcance": "perto",
    "Velocidade": "muito_rápida",
    "Pontos de vida1": "1.060",
    "Dano1": "200",
    "dps1": "250",
    "Pontos de vida2": "1.865",
    "Dano2": "352",
    "dps2": "440"
},

{
    
    "nome": "Balão",
    "Tipo_de_Carta": "aérea",
    "Raridade": "ÉPICA",
    "Alvos": "construções",
    "Alcance": "perto",
    "Velocidade": "média",
    "Pontos de vida1": "1.050",
    "Dano1": "400",
    "danomorre1": "200",
    "dps1": "150",
    "Pontos de vida2": "2.446",
    "Dano2": "932",
    "danomorre2": "466",
    "dps2": "349"
},

{
    
    "nome": "Flechas",
    "Tipo_de_Carta": "Feitiço",
    "Raridade": "COMUM",
    "Alvos": "terrestre-aéreo",
    "Alcance": None,
    "Raio": "1.4",
    "Dano1": "144",
    "dt1": "36",
    "Dano2": "534",
    "dt2": "135"
          
},
{

    "nome": "Mini pekka",
    "Tipo_de_Carta": "terrestre",
    "Raridade": "RARA",
    "Alvos": "terrestre",
    "Alcance": "perto",
    "Velocidade": "rápida",
    "Pontos de vida1": "642",
    "Dano1": "340",
    "dps1": "212",
    "Pontos de vida2": "1.983",
    "Dano2": "1050",
    "dps2": "656"

},

{
 
    "nome": "Bola de fogo",
    "Tipo_de_Carta": "Feitiço",
    "Raridade": "RARA",
    "Alvos": "terrestre-aéreo",
    "Alcance": None,
    "Raio": "2.5",
    "Dano1": "325",
    "dt1": "98",
    "Dano2": "1004",
    "dt2": "302"

},

{

    "nome": "Tronco",
    "Tipo_de_Carta": "Feitiço",
    "Raridade": "LENDÁRIA",
    "Alvos": "terrestre",
    "Alcance": "10,1",
    "Raio": "3,9",
    "Dano1": "290",
    "dt1": "58",
    "Dano2": "422",
    "dt2": "85"
},

{
    "nome": "tesla",
    "Tipo_de_Carta": "construção",
    "Raridade": "COMUM",
    "Alvos": "terrestre-aéreo",
    "Alcance": "5,5",
    "Velocidadeimpact": "1,1",
    "Pontos de vida1": "450",
    "Dano1": "86",
    "dps1": "78",
    "Pontos de vida2": "1.674",
    "Dano2": "319",
    "dps2": "290"
},

{

    "nome": "Esqueletos",
    "Tipo_de_Carta": "terrestre",
    "Raridade": "COMUM",
    "Alvos": "terrestre",
    "Alcance": "perto",
    "Velocidade": "rápida",
    "Pontos de vida1": "32",
    "Dano1": "32",
    "dps1": "32",
    "Pontos de vida2": "119",
    "Dano2": "119",
    "dps2": "119"
}
]

def seguir(continuar):
    if continuar in ["sim", "s"]:
        return True
    elif continuar in ["nao", "n"]:
        return False
    else:
        return None

def cartas():
    cartas = ["cavaleiro", "balão", "balao", "mago", "lenhador", "flechas", "mini pekka", "minipeka" "minipekka", "minepeka", "minepekka", "bola de fogo", "boladefogo", "tesla", "tronco", "esqueletos", "esqueleto"]

    resposta = input("Digite o nome da carta que deseja saber as informações, temos as seguintes cartas disponiveis:\n\nCavaleiro\nBalão\nMago\nLenhador\nFlechas\nMini pekka\nBola de Fogo\nTesla\nTronco\nEsqueleto\n\n").lower().strip()
    while resposta not in cartas:
        print("Resposta inválida, tente novamente\n")
        resposta = input("Digite a carta desejada: ").lower().strip()

    continuar = "sim"
    while continuar not in ["nao", "não", "n"] :
        if resposta == "mago":
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[0]['Tipo_de_Carta']}\n Raridade: {cartas2[0]['Raridade']}\n Alvos: {cartas2[0]['Alvos']}\n Alcance: {cartas2[0]['Alcance']}\n Velocidade: {cartas2[0]['Velocidade']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 3:\n Pontos de vida: {cartas2[0]['Pontos de vida1']}\n Dano: {cartas2[0]['Dano1']}\n DPS: {cartas2[0]['dps1']}\n\n\t NIVEL 15:\n Pontos de vida: {cartas2[0]['Pontos de vida2']}\n Dano: {cartas2[0]['Dano2']}\n DPS: {cartas2[0]['dps2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()

        if resposta == "cavaleiro":
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[1]['Tipo_de_Carta']}\n Raridade: {cartas2[1]['Raridade']}\n Alvos: {cartas2[1]['Alvos']}\n Alcance: {cartas2[1]['Alcance']}\n Velocidade: {cartas2[1]['Velocidade']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 1:\n Pontos de vida: {cartas2[1]['Pontos de vida1']}\n Dano: {cartas2[1]['Dano1']}\n DPS: {cartas2[1]['dps1']}\n\n\t NIVEL 15:\n Pontos de vida: {cartas2[1]['Pontos de vida2']}\n Dano: {cartas2[1]['Dano2']}\n DPS: {cartas2[1]['dps2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()

        if resposta == "lenhador":
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[2]['Tipo_de_Carta']}\n Raridade: {cartas2[2]['Raridade']}\n Alvos: {cartas2[2]['Alvos']}\n Alcance: {cartas2[2]['Alcance']}\n Velocidade: {cartas2[2]['Velocidade']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 9:\n Pontos de vida: {cartas2[2]['Pontos de vida1']}\n Dano: {cartas2[2]['Dano1']}\n DPS: {cartas2[2]['dps1']}\n\n\t NIVEL 15:\n Pontos de vida: {cartas2[2]['Pontos de vida2']}\n Dano: {cartas2[2]['Dano2']}\n DPS: {cartas2[2]['dps2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()

        if resposta in ["balão", "balao"]:
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[3]['Tipo_de_Carta']}\n Raridade: {cartas2[3]['Raridade']}\n Alvos: {cartas2[3]['Alvos']}\n Alcance: {cartas2[3]['Alcance']}\n Velocidade: {cartas2[3]['Velocidade']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 6:\n Pontos de vida: {cartas2[3]['Pontos de vida1']}\n Dano: {cartas2[3]['Dano1']}\n Dano pós morte: {cartas2[3]['danomorre1']}\n DPS: {cartas2[3]['dps1']}\n\n\t NIVEL 15:\n Pontos de vida: {cartas2[3]['Pontos de vida2']}\n Dano: {cartas2[3]['Dano2']}Dano pós morte: {cartas2[3]['danomorre2']}\n DPS: {cartas2[3]['dps2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()
            
        if resposta == "flechas":
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[4]['Tipo_de_Carta']}\n Raridade: {cartas2[4]['Raridade']}\n Alvos: {cartas2[4]['Alvos']}\n Alcance: {cartas2[4]['Alcance']}\n Raio: {cartas2[4]['Raio']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 1:\n Dano: {cartas2[4]['Dano1']}\n Dano na torre: {cartas2[4]['dt1']}\n\n\t NIVEL 15:\n Dano: {cartas2[4]['Dano2']}\n Dano na torre: {cartas2[4]['dt2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()




        if resposta in  ["mini pekka", "minipeka", "minipekka", "minepekka", "minepeka"]:
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[5]['Tipo_de_Carta']}\n Raridade: {cartas2[5]['Raridade']}\n Alvos: {cartas2[5]['Alvos']}\n Alcance: {cartas2[5]['Alcance']}\n Velocidade: {cartas2[5]['Velocidade']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 3:\n Pontos de vida: {cartas2[5]['Pontos de vida1']}\n Dano: {cartas2[5]['Dano1']}\n DPS: {cartas2[5]['dps1']}\n\n\t NIVEL 15:\n Pontos de vida: {cartas2[5]['Pontos de vida2']}\n Dano: {cartas2[5]['Dano2']}\n DPS: {cartas2[5]['dps2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()

        if resposta in  ["bola de fogo", "boladefogo"]:
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[6]['Tipo_de_Carta']}\n Raridade: {cartas2[6]['Raridade']}\n Alvos: {cartas2[6]['Alvos']}\n Alcance: {cartas2[6]['Alcance']}\n Raio: {cartas2[6]['Raio']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 1:\n Dano: {cartas2[6]['Dano1']}\n Dano na torre: {cartas2[6]['dt1']}\n\n\t NIVEL 15:\n Dano: {cartas2[6]['Dano2']}\n Dano na torre: {cartas2[6]['dt2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()

        if resposta == "tronco":
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[7]['Tipo_de_Carta']}\n Raridade: {cartas2[7]['Raridade']}\n Alvos: {cartas2[7]['Alvos']}\n Alcance: {cartas2[7]['Alcance']}\n Largura: {cartas2[7]['Raio']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 1:\n Dano: {cartas2[7]['Dano1']}\n Dano na torre: {cartas2[7]['dt1']}\n\n\t NIVEL 15:\n Dano: {cartas2[7]['Dano2']}\n Dano na torre: {cartas2[7]['dt2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()

        if resposta == "tesla":
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[8]['Tipo_de_Carta']}\n Raridade: {cartas2[8]['Raridade']}\n Alvos: {cartas2[8]['Alvos']}\n Alcance: {cartas2[8]['Alcance']}\n Velocidade de impacto: {cartas2[8]['Velocidadeimpact']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 1:\n Pontos de vida: {cartas2[8]['Pontos de vida1']}\n Dano: {cartas2[8]['Dano1']}\n DPS: {cartas2[8]['dps1']}\n\n\t NIVEL 15:\n Pontos de vida: {cartas2[8]['Pontos de vida2']}\n Dano: {cartas2[8]['Dano2']}\n DPS: {cartas2[8]['dps2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()

        if resposta in ["esqueletos" "esqueleto"]:
            print(f"\n\n\n\n------------------------------------------------------------------------\n\n\t\t INFORMAÇÕES PERMANENTES\n\n Tipo da carta: {cartas2[9]['Tipo_de_Carta']}\n Raridade: {cartas2[9]['Raridade']}\n Alvos: {cartas2[9]['Alvos']}\n Alcance: {cartas2[9]['Alcance']}\n Velocidade: {cartas2[9]['Velocidade']}\n\n------------------------------------------------------------------------\n\n\t ESTATÍSTICAS QUE MUDAM DE ACORDO COM O NIVEL\n\n\t NIVEL 1:\n Pontos de vida: {cartas2[9]['Pontos de vida1']}\n Dano: {cartas2[9]['Dano1']}\n DPS: {cartas2[9]['dps1']}\n\n\t NIVEL 15:\n Pontos de vida: {cartas2[9]['Pontos de vida2']}\n Dano: {cartas2[9]['Dano2']}\n DPS: {cartas2[9]['dps2']}\n\n------------------------------------------------------------------------  ")
            continuar = input("\nQuer ver as informações de outra carta? ").lower().strip()
            if seguir(continuar) == True:
                resposta = input("Digite a carta desejada: ").lower().strip()

            elif seguir(continuar) == False:
                break

            else:
                print("Comando não identificado, tente novamente:\n")
                resposta = input("Digite a carta desejada: ").lower().strip()


    
cartas()
