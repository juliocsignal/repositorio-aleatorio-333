from random import randint
nomes = []
b = ""
cont = 0
while (b != "1"):
    nomes.append(input("Digite um nome para sorteio! "))
    cont = cont + 1
    b = input()

sorte = randint(0,cont)

print("O vencedor é: ", nomes[sorte])
