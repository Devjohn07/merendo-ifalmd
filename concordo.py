

def main():
    boool = input("Você concorda? ").strip().lower()
    concordo1 = concordo(boool)

    if concordo1 == True:
        print("concordo")

    elif concordo1 == False:
        print("Não Concordo")
    
    else:
        print("comando não identificado")


def concordo(boool):
    if boool in  ["sim", "s"]: return True

    elif boool in ["não", "nao", "n"]:  return False

    else: return None


main()