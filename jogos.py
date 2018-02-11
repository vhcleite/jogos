import advinhacao
import forca
import zelda
import mario

def iniciar_jogo():
    #print("Escolha o jogo\n(1) Advinhação\n(2) Forca\n(3) Zelda\n(4) Mario")
    print("###################")
    print("Escolha um jogo: ")
    print("1 - Advinhação")
    print("2 - Forca")
    print("3 - Zelda")
    print("4 - Mario")
    print("###################")

    escolha = int(input("Número do jogo: "))
    print("Você escolheu ", escolha)

    if (escolha == 1):
        advinhacao.jogar()
    elif(escolha == 2):
        forca.jogar()
    elif(escolha == 3):
    	zelda.jogar()
    elif(escolha == 4):
    	mario.jogar()

if(__name__ == "__main__"):
    iniciar_jogo()
    #testando o git add -i