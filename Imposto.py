from random import *
cont = 5
nomed = []
nomed.append("Menino do Galvão")
nomed.append("Narizinho")
nomed.append("Família Real")
nomed.append("Namoradinho do Neymar")
nomed.append("Patricinha da Friboi")
nomed.append("Amigo do Lula")

while (cont != 0):
    senha = input("Qual a senha?")

    if (senha == "IMPOSTO É ROBÔ"):
        cont = 0
        print("Vamos jogar, padawan! ")
        nome = input("Pra começar diga seu nome! ")
        print(nome,",","seu nome de sonegador é: ", nomed[randint(0,5)])
        
        
    else:
        cont = cont - 1
        print("VOCÊ ERROU SEU ESTATISTA DO CARALHO")
        print("Você tem mais",cont,"chances! ")
