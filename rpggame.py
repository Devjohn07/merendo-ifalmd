import random
import time

interagir = 0
inventário = {}
resistencia, vitalidade, força, reaçao, arcano =  1, 10, 1, 1, 1
pontos = 10
weapon = "nenhuma"

def girarD20():
   global valor_aleatorio
   valor_aleatorio = random.randint(1, 20)
   print(f'\n"um dado foi rolado para testar a sua sorte"\n')

#Escolhe um atributo para ser usado  
def usar_atributo(valor):
   atributo = input("Qual atributo deseja usar?\nVITALIDADE: Reduz o dano recebido\nFORÇA: Adiciona dano a armas corpo-a-corpo, porém, diminui a chance de acerto\nreação: Dependendo, você pode desviar do ataque eminente, porém existe a chance de n desviar e receber dano completo\n")
   if atributo == "resistencia":
      total = resistencia + valor
      print(f"Vou girar um d20+{resistencia}") 
      print(f"você tirou {total} no dado!")

#imprime o inventário no menu
def imprimir_inventario(inventário):
    print("Inventário:")
    for item, quantidade in inventário.items():
        print(f"{item}: {quantidade}")

#Verifica a quantidade de intens no inventário(usado principalmente para que o usuário sempre pegue uma quantidade especifica de itens nas cenas)
def verificar_quantidade(inventário, item):
    if item in inventário and inventário[item] >= 1:
        return True
    else:
        return False

def adicionar_item(inventário, item, quantidade):
    # Se o item já está no inventário, apenas aumenta a quantidade
    if item in inventário:
        inventário[item] += quantidade
    # Caso o item não exista, ele é adicionado com a quantidade informada
    else:
        inventário[item] = quantidade
    print(f"\n{quantidade} unidades de {item} foram adicionadas.")
"""
Usando a função para adicionar 20 munições
adicionar_item(inventario, "munição", 20)
print(f"Agora você tem {inventario['munição']} munições.")
"""

#menu do jogo
def menu():


   while resposta1 not in ("continuar", "interagir", "atacar", "usar atributo", "comandos"):
      global weapon
      global pontos
      global resistencia, vitalidade, força, reaçao, arcano
      print("---------------------------------------------------------------------------------------------------------------------------")
      print("""                               __  __ ______ _   _ _    _ 
                              |  \/  |  ____| \ | | |  | |
                              | \  / | |__  |  \| | |  | |
                              | |\/| |  __| | . ` | |  | |
                              | |  | | |____| |\  | |__| |
                              |_|  |_|______|_| \_|\____/ 
                             """)
      print("---------------------------------------------------------------------------------------------------------------------------")

      #mostra as opções de menu, atributos e itens  no inventário
      {imprimir_inventario(inventário)}
      print(f" \nATRIBUTOS:\n\t--------------------------------\n\t\tvitalidade: {vitalidade}\n\t--------------------------------\n\t\tresistencia: {resistencia}\n\t--------------------------------\n\t\tforça: {força}\n\t--------------------------------\n\t\treação: {reaçao}\n\t--------------------------------\n\t\tarcano: {arcano}\n\t--------------------------------\n Você tem {pontos} pontos para gastar nos atributos")
      optionsmenu = int(input("---------------------------------------------------------------------------------------------------------------------------\n\t\t\t\t\t\t OPÇÕES DO MENU\n---------------------------------------------------------------------------------------------------------------------------\n\ngastar pontos[1]\ninspecionar itens[2]\nTutorial do menu[3]\nSair do menu[4]\n"))
      
      #faz a distribuição de pontos
      if optionsmenu == 1:
         if pontos <= 0:
            print("você não possui pontos para gastar\n")
            optionsmenu = int(input("---------------------------------------------------------------------------------------------------------------------------\n\t\t\t\t\t\t OPÇÕES DO MENU\n---------------------------------------------------------------------------------------------------------------------------\n\ngastar pontos[1]\ninspecionar itens[2]\nTutorial do menu[3]\nSair do menu[4]\n"))
         pontosgastos =int(input("quantos pontos quer gastar?\n"))
         atributo = input("em qual atributo?\n")
         if atributo == "vitalidade":
            vitalidade += pontosgastos
            pontos -= pontosgastos
            print(f"OK, pontos foram gastos")
         elif atributo == "força":
            força += pontosgastos
            pontos -= pontosgastos
            print(f"OK, pontos foram gastos")
         elif atributo == "reação":
            reaçao += pontosgastos
            pontos -= pontosgastos
            print(f"OK, pontos foram gastos")
         elif atributo == "arcano":
            arcano += pontosgastos
            pontos -= pontosgastos
            print(f"OK, pontos foram gastos")
         elif atributo == "resistencia":
            resistencia += pontosgastos
            pontos -= pontosgastos
            print(f"OK, pontos foram gastos")

      #inspeciona os itens que tem no inventário
      #números dado para cada item no jogo: faca[1], pistola[2], munição[3], roupas_limpas[4]
      if optionsmenu == 2:
         if inventário == True:
            print(inventário)
            item = int(input("qual item quer inspecionar?"))
            if item == 1:
               if verificar_quantidade() == True:
                  print("uma faca que você encontrou numa gaveta no quarto inicial, simples porém efetiva(1d5 de dano sem bonus externos)")
            if item == 2:
               if verificar_quantidade() == True:
                  print("uma pistola encontrada no quarto incial, encontrada sem balas, será que tem algumas por ai?(1d10 de dano sem bonus externos)")
            if item == 3:
               if "munição[3]" in inventário:
                  if verificar_quantidade() == True:
                     print("Uma simples mnição que muda de acordo com a arma, ela não é tão forte, porém funciona(+2 no dano com qualquer arma)")
            if item == 4:
               if verificar_quantidade() == True:
                  print("roupas limpas, elas possuem uma defesa razoável e são definitivamente seguras(+5 vitalidade)")
         else:
            print("\nSeu inventário está vazio\n")

      #faz um tutorial para explicar as funcionalidades do menu
      if optionsmenu == 3:
         print("\nATRIBUTOS: São seus status, oque define sua vida, sua força, seu nivel de reação\n\tVITALIDADE: Defini sua vida, se ela zerar, acabou\n\tFORÇA: define o quão forte você é e ajuda em testes que exijam força fisica\n\tREAÇÃO: define sua velocidade de reação, usada em testes que peça ao personagem para desviar de algo\n\tRESISTÊNCIA: Ajuda em testes que exijam resistência(tanto fisica quanto mentaL)\n\tARCANO: melhora sua sorte para achar itens e também aumenta dano de armas elementais\n")
         print("INVENTÁRIO: Usado para mostrar quais itens você possui guardado\n")
         
      #simplesmente sai do menu
      if optionsmenu == 4:
         break
#titulo do jogo e começo da primeira cena
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
print("comandos:\ncontinuar\ninteragir\natacar\nmenu\ncomandos")
print("\n\n")
time.sleep(2)
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

#Acaba de acordar
while resposta1 not in ["menu", "interagir", "atacar", "continuar", "comandos"]:
    print("comando não identificado, tente novamente")
    resposta1 = input("O que quer fazer?\n")

while resposta1 not in "continuar":
    if resposta1 == "menu":
      menu()
      resposta1 = input("O que quer fazer?\n")
    elif resposta1 == "atacar":
     print("\nvocê socou o ar, nada acontece\n")

    elif resposta1 == "interagir":
        print("\nvocê fechou a cortina, agr você enxerga melhor\n")
        interagir = 1

    elif resposta1 == "comandos":
       print("\nAqui estão todos os comandos possiveis:\ncontinuar\ninteragir\natacar\nmenu\nusar atributo\ncomandos\n")

    elif resposta1 not in ["menu", "interagir", "atacar", "continuar"]:
       print("\ncomando não identificado, tente novamente")
    resposta1 = input("O que quer fazer?\n")

if resposta1 == "continuar":
   if interagir == 1:
    print("\npercebe-se que tu se encontras em um quarto estranhamente familiar, porém você não faz a menor idéia de onde esteja(o quarto não parece ter nada de mais)\n")
   elif interagir == 0:
      print("\nComo vai continuar sem exergar? O ADM abre a cortina a cortina para ti. percebe-se que tu se encontras em um quarto estranhamente familiar, porém você não faz a menor idéia de onde esteja(o quarto não parece ter nada de mais)\n")

resposta1 = input("O que quer fazer?\n")

#você exerga e vê o quarto
while resposta1 not in "continuar":
   if resposta1 == "menu":
      menu()
      resposta1 = input("O que quer fazer?\n")
   elif resposta1 == "interagir":
       interaçoes = input("\ncom o que deseja interagir?\ngaveta\narmário\njanela\ncama\n\n") 
       #usado para ver o que tem dentro da cada interação
       if interaçoes == "gaveta":
         if verificar_quantidade(inventário, "pistola[2]") and verificar_quantidade(inventário, "faca[1]"):
            print("\nNão tem nada aqui(NÃO INSISTA!)\n")

         elif "pistola[2]" in inventário:
           print("você abre a gaveta, tem uma uma faca dentro.")
           yesnot = input("o que você quer pegar?\nfaca\n\nOBS: digite exatamente como escrito acima para que prossiga\n\n")
           if yesnot == "faca":
            print("pegou a faca")
            adicionar_item(inventário, "faca[1]", 1)
            print(f"Agora você tem {inventário['faca[1]']}")
            resposta1 = input("O que quer fazer?\n")

         elif "faca[1]" in inventário:
             print("você abre a gaveta, tem uma pistola dentro.")
             yesnot = input("o que você quer pegar?\npistola\n\nOBS: digite exatamente como escrito acima para que prossiga\n\n")
             if yesnot == "pistola":
               print("pegou a pistola[2]")
               adicionar_item(inventário, "pistola[2]", 1)
               print(f"Agora você tem {inventário['pistola[2]']}")
               resposta1 = input("O que quer fazer?\n")

            #aqui já foi uma farm infinita de item(bons tempos que não voltam mais)

         else:
             print("\nvocê abre a gaveta, tem uma pistola e uma faca dentro.\n")
             yesnot = input("o que você quer pegar?\nfaca\npistola\n\nOBS: digite exatamente como escrito acima para que prossiga\n")
             if yesnot == "pistola":
               print("pegou a pistola[2]")
               adicionar_item(inventário, "pistola[2]", 1)
               print(f"Agora você tem {inventário['pistola[2]']} pistola\n")
               resposta1 = input("O que quer fazer?\n")
             elif yesnot == "faca":
               print("pegou a faca")
               adicionar_item(inventário, "faca[1]", 1)
               print(f"Agora você tem {inventário['faca[1]']} faca\n")
               resposta1 = input("O que quer fazer?\n")

       elif interaçoes == "armário":
         if interagir == 2:
            print("Sem mais interações por aqui\n")
            resposta1 = input("O que quer fazer?\n")
         if interagir != 2:
            girarD20()
            valor_aleatorio += arcano
            if valor_aleatorio < 10:
               print("não tem nada no armário")
               interagir = 2
               valor_aleatorio -= arcano
               resposta1 = input("O que quer fazer?\n")
            else:
               yesnot = input("Tem um cesto de roupas, quer dar uma olhada?\nsim\nnao\n")
               if yesnot == "sim":
                  girarD20()
                  if valor_aleatorio < 10:
                     print("tinha várias aranhas, elas pularam na sua cara, você se espantou e fechou o armário")
                     interagir = 2
                     valor_aleatorio -= arcano
                     resposta1 = input("O que quer fazer?\n")
                  else:
                     print("Você achou roupas limpas!")
                     adicionar_item(inventário, "roupas_limpas[4]", 1)
                     interagir = 2
                     resposta1 = input("O que quer fazer?\n")

       elif interaçoes not in ["gaveta", "armário", "janela", "cama"]:
         print("\nComando não identificado")
         resposta1 = input("O que quer fazer?\n")
   elif resposta1 == "atacar":
     print("você socou o ar, nada acontece\n")


   elif resposta1 == "comandos":
       print("Aqui estão todos os comandos possiveis:\ncontinuar\ninteragir\natacar\nmenu\nusar atributo\ncomandos\n")

   elif resposta1 not in ["menu", "interagir", "atacar", "norte", "sul", "oeste", "leste", "usar atributo" ]:
       print("comando não identificado, tente novamente")
       resposta1 = input("O que quer fazer?\n")

if resposta1 == "continuar":
    print("\nvocê saiu do quarto, você está em um corredor com várias portas\n")
