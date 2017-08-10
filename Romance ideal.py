import matplotlib.pyplot as plt

salar = [] #salario de todos em um array
total = [] #salário + abono de todos em um array
aux = -1
i = 0
abono = []

while (aux != 0):
    aux = int(input("Digite seu salário! : "))
    salar.append(aux)
    abono.append(aux*0.2)
    if (abono[i] < 100):
            abono[i] = 100;
    total.append(salar[i]+abono[i])
    i = i + 1
abono.pop(-1)
salar.pop(-1)
total.pop(-1)

print("Salários + abono: ",total)
print("Abonos",abono)
