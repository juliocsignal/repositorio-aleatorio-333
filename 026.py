class Oi():
    #Nome dos Funcionários
    fnc = []

    #Espaço antes da conversão
    esp = []

    #Espaço depois da conversão
    espd = []

    #Valor total em MB (declaração)
    value = 0

    #Cálculo de porcentagem (declaração)
    pcento = []

    #Espaço de formatação
    forma = []

    #Arrendondar

    def arredondar(num):
        return float( '%g' % ( num ))

    #Atribuição de nomes
    fnc.append("Alexandre")
    fnc.append("Anderson")
    fnc.append("Antonio")
    fnc.append("Carlos")
    fnc.append("Cesar")
    fnc.append("Rosemary")

    #Atribuição de espaço utilizado
    esp.append(int(456123789))
    esp.append(int(1245698456))
    esp.append(int(123456456))
    esp.append(int(91257581))
    esp.append(int(987458))
    esp.append(int(789456125))

    #Conversão de valor
    for i in range(6):
        div = arredondar(esp[i] / 1024)
        espd.append(arredondar(div / 1024))

    #Valor total em MB

        value = value + espd[i]

    #Cálculo de porcentagem
    for i in range(6):
        pcento.append(espd[i] / value * 100)

    #Impressão de valores
    print("JCGJ Inc.                 Uso do espaço em disco pelos usuários")
    print("------------------------------------------------------------------------------")

    i = 1


    print(i,fnc[0]," ","%.2f" % espd[0],"MB","   ","%.2f" % pcento[0],"%")
    print(i+1,fnc[1]," ","%.2f" % espd[1],"MB","   ","%.2f" % pcento[1],"%")
    print(i+2,fnc[2],"   ","%.2f" % espd[2],"MB","    ","%.2f" % pcento[3],"%")
    print(i+3,fnc[3],"     ","%.2f" % espd[3],"MB","    ","%.2f" % pcento[3],"%")
    print(i+4,fnc[4],"       ","%.2f" % espd[4],"MB","    ","%.2f" % pcento[4],"%")
    print(i+5,fnc[5],"  ","%.2f" % espd[5],"MB","   ","%.2f" % pcento[5],"%")

    l = input()
