
def jogar():
    print("*******************************")
    print("Bem vindo ao jogo da forca")
    print("*******************************")


    palavra_secreta = "cachorro"

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        chute = input("Digite uma letra: ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if letra.upper() == chute.upper():
                print("Encoutrou '{}' na posição '{}'".format(letra, index))
            index = index + 1

    print("*** Fim de Jogo ***")

if(__name__ == "__main__"):
	jogar()