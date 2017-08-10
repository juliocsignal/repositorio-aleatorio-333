def CalcMes():
    soma = "0"
    contas = []
    nomec = []
    cont = 0
    while (soma != "1"):
        nomec.append(input("Crie um rótulo para a conta: "))
        contas.append(int(input("Insira o valor:  ")))
        cont = cont + 1
        soma = input("Para parar, digite 1!")

    for i in range(cont):
        print(nomec[i],":",contas[i])
        result = sum(contas)
    print("O somatório das contas é igual a:",result)

CalcMes()
