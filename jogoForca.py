#
# Jogo "Forca"
# 
def exibeForca(p,e):
    print("+-----+")
    print("|     |")
    print("|     O")
    print("|    -|-")
    print("|    | |")
    print("|")
    print("|=======| ",p, "( ",e,"erros de 5)")

print ('----- INÍCIO DA EXECUÇÃO -----')
import random
listaPalavras=["cavalo","aranha","ornitorrinco","girafa","golfinho"]
palavraSort = listaPalavras[random.randrange(0,4)]

print(">>>>Palavras sorteada:",palavraSort)
palavraJog = ""
palavraJog = palavraJog.rjust(len(palavraSort),".")
erros = 0
while True:
    # ----- exibe a forca -----
    exibeForca(palavraJog,erros)
    # ----- pede uma nova letra -----
    letra = input("Letra? ")
    # ----- verifica se a letra existe na palavra sorteada -----
    i = 0
    for x in palavraSort:
        if (letra == x):
            palavraJog = palavraJog[:i] + letra + palavraJog[i+1:]
        i += 1
    if (palavraJog == palavraSort):
        print("Parabéns! Você acertou a palavra secreta.")
        break
    elif (erros > 5):
            print("Fim de jogo. Você errou mais de 5 letras")
            break
        elif ()
                                
print('----- FIM DA EXECUÇÃO: -----')