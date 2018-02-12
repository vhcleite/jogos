import random


def mostrar_mensagem_abertura():
    print("*******************************")
    print("Bem vindo ao jogo da forca")
    print("*******************************")


def escolher_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for line in arquivo:
        line = line.strip()
        palavras.append(line)

    arquivo.close()

    numero_aleatorio = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_aleatorio].upper()
    return palavra_secreta


def inicializar_palavra_acertada(palavra_secreta):
    palavra_acertada = ["_" for letra in palavra_secreta]  # utilizando list comprehensions
    return palavra_acertada


def pegar_chute_jogador():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute


def encontrar_letras_na_palvra(palavra_secreta, chute, palavra_acertada):
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            palavra_acertada[index] = letra
        index += 1


def jogar():
    mostrar_mensagem_abertura()
    palavra_secreta = escolher_palavra_secreta()
    palavra_acertada = inicializar_palavra_acertada(palavra_secreta)
    print(palavra_acertada)

    acertou = False
    enforcou = False
    tentativas = 6

    while(not acertou and not enforcou):
        chute = pegar_chute_jogador()

        if(chute in palavra_secreta):
            encontrar_letras_na_palvra(palavra_secreta, chute, palavra_acertada)
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