menu = 0
inventário = []
vitalidade, força, reaçao, = 100, 10, 10
pontos = 0
weapon = "nenhuma"
sorte = 5
interagir = 0


#titulo do jogo
print ("---------------------------------------------------------------------------------------------------------------------------")
print("""              _____          ____          _   _          
     /\      / ____|   /\   |  _ \   /\   | \ | |   /\    
    /  \    | |       /  \  | |_) | /  \  |  \| |  /  \   
   / /\ \   | |      / /\ \ |  _ < / /\ \ | . ` | / /\ \  
  / ____ \  | |____ / ____ \| |_) / ____ \| |\  |/ ____ \ 
 /_/    \_\  \_____/_/    \_\____/_/    \_\_| \_/_/    \_\
                                                          
                                                           """)
print ("---------------------------------------------------------------------------------------------------------------------------")
print("jogo feito pelo Paulino ;)")
print("comandos:\ncontinuar\ninteragir\natacar\nmenu\nusar atributo\ncomandos")
print("\n\n")
print("""       _.-'''-._
     .'   .-'``|'.
    /    /    -*- 
   ;   <{      |   ;
   |    _\ |       | 
   ;   _\ -*- |    ;
    \   \  | -*-  /
     '._ '.__ |_.'
        '-----'
""")
print("Você acorda com o brilho da lua em sua face, praticamente cegando-te, A única coisa visivel é uma cortina branca")
resposta1 = input("O que quer fazer?\n")

#Acaba de acordar, opções da primeira cena
while resposta1 not in ["menu", "interagir", "atacar", "continuar", "comandos", "usar atributo" ]:
    print("comando não identificado, tente novamente")
    resposta1 = input("O que quer fazer?\n")

while resposta1 not in "continuar":
    if resposta1 == "menu":
      print("---------------------------------------------------------------------------------------------------------------------------")
      print("""                               __  __ ______ _   _ _    _ 
                              |  \/  |  ____| \ | | |  | |
                              | \  / | |__  |  \| | |  | |
                              | |\/| |  __| | . ` | |  | |
                              | |  | | |____| |\  | |__| |
                              |_|  |_|______|_| \_|\____/ 
                             """)
      print("---------------------------------------------------------------------------------------------------------------------------")
      print(f"   ATIBUTOS:\n\t--------------------------------\n\t\tvitalidade: {vitalidade}\n\t--------------------------------\n\t\t  força: {força}\n\t--------------------------------\n\t\t  reação: {reaçao}\n\t--------------------------------\n\t\t  sorte: {sorte}\n\t--------------------------------")

    elif resposta1 == "atacar":
     print("você socou o ar, nada acontece\n")

    elif resposta1 == "interagir":
        print("você fechou a cortina, agr você enxerga melhor\n")
        interagir = 1

    elif resposta1 == "usar atributo":
       print("nenhum atributo pode ser usado aqui\n")

    elif resposta1 == "comandos":
       print("Aqui estão todos os comandos possiveis:\ncomandos:\nnorte\nsul\nleste\noeste\npiscar\ninteragir\natacar\nmenu\nusar atributo\ncomandos\n")

    elif resposta1 not in ["menu", "interagir", "atacar", "continuar", "usar atributo" ]:
       print("comando não identificado, tente novamente")
    resposta1 = input("O que quer fazer?\n")

if resposta1 == "continuar":
   if interagir == 1:
    print("percebe-se que tu se encontras em um quarto estranhamente familiar, porém você não faz a menor idéia de onde esteja(o quarto não parece ter nada de mais)")
   elif interagir == 0:
      print("Como vai continuar sem exergar? O ADM abre a cortina a cortina para ti. percebe-se que tu se encontras em um quarto estranhamente familiar, porém você não faz a menor idéia de onde esteja(o quarto não parece ter nada de mais)\n")

resposta1 = input("O que quer fazer?\n")

#você exerga e vê o quarto
while resposta1 not in "continuar":

    if resposta1 == "menu":
      print("---------------------------------------------------------------------------------------------------------------------------")
      print("""                               __  __ ______ _   _ _    _ 
                              |  \/  |  ____| \ | | |  | |
                              | \  / | |__  |  \| | |  | |
                              | |\/| |  __| | . ` | |  | |
                              | |  | | |____| |\  | |__| |
                              |_|  |_|______|_| \_|\____/ 
                             """)
      print("---------------------------------------------------------------------------------------------------------------------------")
      print(f"   ATIBUTOS:\n\t--------------------------------\n\t\tvitalidade: {vitalidade}\n\t--------------------------------\n\t\t  força: {força}\n\t--------------------------------\n\t\t  reação: {reaçao}\n\t--------------------------------\n\t\t  sorte: {sorte}\n\t--------------------------------")

    elif resposta1 == "interagir":
       interaçoes = input("com o que deseja interagir?\ngaveta\narmário\njanela\ncama\n\n") 
       if interaçoes == "gaveta":
          print("você abre a gaveta, tem uma pistola e uma faca dentro.")
          yesnot = input("o que você quer pegar?\nfaca\npistola\ntodos\n\nOBS: digite exatamente como escrito acima para que prossiga\n\n")

          if yesnot == "faca":
           print("pegou a faca")
           inventário.append("faca")
           resposta1 = input("O que quer fazer?\n")
          elif yesnot == "pistola":
           print("pegou a pistola")
           inventário.append("pistola")
           resposta1 = input("O que quer fazer?\n")
          elif yesnot == "todos":
           print("você pegou todos os itens")
           inventário.extend(["pistola", "faca"])
           resposta1 = input("O que quer fazer?\n")
    elif resposta1 == "atacar":
     print("você socou o ar, nada acontece\n")

    elif resposta1 == "usar atributo":
       print("nenhum atributo pode ser usado aqui\n")

    elif resposta1 == "comandos":
       print("Aqui estão todos os comandos possiveis:\ncomandos:\nnorte\nsul\nleste\noeste\npiscar\ninteragir\natacar\nmenu\nusar atributo\ncomandos\n")

    elif resposta1 not in ["menu", "interagir", "atacar", "norte", "sul", "oeste", "leste", "usar atributo" ]:
       print("comando não identificado, tente novamente")
       resposta1 = input("O que quer fazer?\n")

if resposta1 == "continuar":
    print("você saiu do quarto, você está em um corredor com várias portas\n")

resposta1 = input("O que quer fazer?\n")