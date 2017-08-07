def EqSegGrau():
    print("Vamos calcular Equações do Segundo Grau!")
    exe = 0
    while (exe != "1"):
        a = float(input("Digite o primeiro coeficiente!"))
        b = float(input("Digite o segundo coeficiente!"))
        c = float(input("Digite o terceiro coeficiente!"))
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

        exe = input("Para parar digite 1!")

EqSegGrau()

print("Oi")