import random

def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1, 101)
    print("numero secreto: ",numero_secreto)

    total_tentativas = 0
    iteracao = 1
    pontuacao = 1000


    print("(1) fácil (2) médio (3) difícil")
    nivel = int(input("Dificuldade: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for iteracao in range(1,total_tentativas + 1):
        print("Iteração", iteracao, "de", total_tentativas, numero_secreto)
        #print("Iteração {} de {}". format(iteracao, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        chute_int = int(chute_str)
        print("Você digitou: ", chute_int)

        if(chute_int < 1 or chute_int > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute_int == numero_secreto
        maior   = chute_int > numero_secreto
        menor   = chute_int < numero_secreto

        if(acertou):
            print("Você ACERTOU")
            break
        else:
            if(maior):
                print("Você ERROU com um número maior")
            elif(menor):
                print("Você ERROU com um número menor")
            pontuacao = pontuacao - (abs(chute_int - numero_secreto)/3)
    print("Você fez {} pontos". format(pontuacao))
    print("*** Fim de Jogo ***")

if(__name__ == "__main__"):
	jogar()