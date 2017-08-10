#lista de perguntas feitas pela polícia
a = []
aux = 0
a.append("Telefonou para a vítima? ")
a.append("Esteve no local do crime? ")
a.append("Mora perto da vítima? ")
a.append("Devia para a vítima? ")
a.append("Já trabalhou para a vítima? ")


for i in range(5):
    resp = input(a[i])
    if (resp == "S"):
        aux = aux + 1

if (aux == 5):
    print("VOCÊ É O ASSASSINO")

if (aux == 3 or aux == 4):
    print("VOCÊ É O CÚMPLICE")

if (aux == 2):
    print("VOCÊ É UM SUSPEITO")

if (aux == 1):
    print("Você é inocente!")

print (aux)
input("Digite 'ENTER' para sair")
