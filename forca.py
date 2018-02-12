
def jogar():
    print("*******************************")
    print("Bem vindo ao jogo da forca")
    print("*******************************")


    palavra_secreta = "cachorro".upper()
    palavra_acertada = ["_", "_", "_", "_", "_", "_", "_", "_"]
    acertou = False
    enforcou = False
    tentativas = 6

    print(palavra_acertada)
    while(not acertou and not enforcou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if letra == chute:
                    palavra_acertada[index] = letra
                    print("Encoutrou '{}' na posição '{}'".format(letra, index))
                index += 1
        else:
            tentativas -= 1
            print("Faltam {} tentativas".format(tentativas))
            if ((tentativas == 0)):
                enforcou = True
                print("ENFORCOU")

        if ("_" not in palavra_acertada):
            print("Você VENCEU  ")
            acertou = True

        print(palavra_acertada)

    print("*** Fim de Jogo ***")

if(__name__ == "__main__"):
	jogar()