import advinhacao
import forca

def iniciar_jogo():
    print("Escolha o jogo\n(1) Advinhação\n(2) Forca")

    escolha = int(input("Escolha: "))
    print("Você escolheu ", escolha)

    if (escolha == 1):
        advinhacao.jogar()
    elif(escolha == 2):
        forca.jogar()

if(__name__ == "__main__"):
    iniciar_jogo()