c = False

while (c != True):
    from random import *
    a = randint(0,10)
    b = int(input("Adivinhe um número de 1 a 10!: "))
    c = b == a


    if (c == True):
        print("PARABÉNS, VOCÊ GANHOU!")
    else:
        print("Que pena, não foi dessa vez!")

