from random import randint

def Aleatorio():
    b = 0
    i = 0

    while (b != 13898):
        b = randint(0,16000)
        i = i + 1


    print("Foram necessárias",i,"execuções aleatórias para se chegar ao valor",b)
Aleatorio()

