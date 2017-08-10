from random import randint

def Sorte():
    cash = 1000
    stop = 0
    last = []
    i = 0

    last.append(0)

    print("Você possui",cash,"reais.")

    while (stop != 1):
        
        strcash = input("Digite o valor da aposta! ")        
        
        aposta = int(strcash)

        print("O último número foi:",last[i])
        
        value = int(input("Insira o número a ser sorteado! "))

        b = randint(0,9)
        
        tf = value == b
        
        if (tf == True):
            cash = cash + aposta
            print("Você acertou! =P")
            print("Você possui",cash,"reais.")

        if (tf == False):
            cash = cash - aposta
            print("Você errou! :(")
            print("Você possui",cash,"reais. ")
        if (cash == 2000):
            stop = 1
            print("VOCÊ GANHOU! ")
        if (cash <= 0):
            stop = 1
            print("VOCÊ PERDEU! ")

        i = i + 1

        last.append(b)
        
    sair = input("Enter para sair")

Sorte()
