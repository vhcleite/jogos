
def jogar():
    print("*******************************")
    print("Bem vindo ao jogo da forca")
    print("*******************************")


    palavra_secreta = "cachorro"

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        chute = input("Digite uma letra: ")
        index = 0
        for letra in palavra_secreta:
            if letra == chute:
                print("Encoutrou '{}' na posição '{}'".format(letra, index))
            index = index + 1

    print("*** Fim de Jogo ***")

if(__name__ == "__main__"):
	jogar()