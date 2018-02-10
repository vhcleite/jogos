import advinhacao
import forca
import zelda

def iniciar_jogo():
    print("Escolha o jogo\n(1) Advinhação\n(2) Forca\n(3) Zelda")

    escolha = int(input("Escolha: "))
    print("Você escolheu ", escolha)

    if (escolha == 1):
        advinhacao.jogar()
    elif(escolha == 2):
        forca.jogar()
    elif(escolha == 3):
    	zelda.jogar()

if(__name__ == "__main__"):
    iniciar_jogo()
    #testando o git add -i