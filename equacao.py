import matplotlib.pyplot as plt

a = float(input("Digite o primeiro coeficiente!"))
b = float(input("Digite o segundo coeficiente!"))
c = float(input("Digite o terceiro coeficiente!"))

e = []



#Formação da equação

if (a > 0 and b > 0 and c > 0):
    print("A sua equação é:",a,"x² +",b,"x +",c)

if (a > 0 and b < 0 and c > 0):
    print("A sua equação é:",a,"x²",b,"x +",c)

if (a > 0 and b < 0 and c < 0):
    print("A sua equação é:",a,"x²",b,"x",c)

if (a < 0 and b > 0 and c < 0):
    print("A sua equação é:",a,"x² +",b,"x",c)

if (a < 0 and b < 0 and c > 0):
    print("A sua equação é:",a,"x²",b,"x +",c)

if (a > 0 and b > 0 and c < 0):
    print("A sua equação é:",a,"x² +",b,"x",c)

if (a < 0 and b < 0 and c < 0):
    print("A sua equação é:",a,"x²",b,"x",c)

if (a < 0 and b > 0 and c > 0):
    print("A sua equação é:",a,"x² +",b,"x +",c)
        
#Orientação do gráfico

if (a == 0):
    print("Esta equação não é de Segundo Grau!")

else:
    if (a > 0):
        print("Concavidade voltada para cima!")
        
    if (a < 0):
        print("Concavidade voltada para baixo!")

    #Cálculo do Delta

    delta = b**2 - (4*a*c)

    #Determinação das Raízes e Cálculo de Bháskara

    if (delta < 0):
        print("Esta equação não possui raízes reais! ")

    if (delta > 0):
        print("Esta equação possui duas raízes! ")
        x1 = (-b +(delta**0.5))/(2*a)
        x2 = (-b -(delta**0.5))/(2*a)
        x1 = round(x1,2)
        x2 = round(x2,2)
        print("As raízes desta equação são:",x1,"e",x2)

    if (delta == 0):
        print("Esta equação possui apenas uma raiz! ")
        x1 = (-b +(delta**0.5))/(2*a)
        x1 = round(x1,2)
        print("A raiz desta equação é:",x1)

    

for i in range(-10,10):
    e.append(i)
r = []

for i in range(len(e)):
    r.append(a*(e[i]**2) + b*e[i] + c )

for i in range(len(r)):
    print ("Equação em função de",i-10,r[i])

#Criação do gráfico
plt.plot((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),'r-')
#plt.plot((r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],x1,r[10],x2,r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19]),'b-')
plt.plot((r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],x1,x2,r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19]),'g-')




plt.title("Gráfico da Equação Descrita")
plt.show()
