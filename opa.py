from funcoes import *
import matplotlib.pyplot as plt



#Cálculos de Arranjo

def Arranjo(n,p):
    nf = Fatorial(n)

    pf = Fatorial(p)

    dif = Fatorial(n-p)

    A = nf/(dif)

    return A


#Cálculos de fatorial

def Fatorial(x):
    fatorial = x
    x = x - 1

    while (x > 1):
        fatorial = fatorial * x
        x = x - 1

    return fatorial

#Cálculos de Combinação

def Combina(n,p):

    nf = Fatorial(n)

    pf = Fatorial(p)

    dif = Fatorial(n-p)

    C = nf/(pf*dif)

    return C

#Cálculo das Probabilidades

def Probabilidade(favoraveis,possibilidades):
    Prob = favoraveis / possibilidades * 100

    return Prob


n = 61

p = 6

resp = int(Arranjo(n,p))

favoraveis = 3

prov = Probabilidade(favoraveis,resp)

plt.plot((0,resp),'g-')
plt.plot((0,favoraveis*100),'b-')
plt.show()

print(resp,favoraveis)

#print(round(prov,8),"%")
