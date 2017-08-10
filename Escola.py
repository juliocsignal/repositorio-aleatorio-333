nome = []
p1 = []
p2 = []
p3 = []
p4 = []
media = []
aux = 0

for i in range(10):
    nome.append(input("Insira o nome do aluno: "))
    print("O número desse aluno é", i)
    p1.append(float(input("Insira a nota da P1: ")))
    p2.append(float(input("Insira a nota da P2: ")))
    p3.append(float(input("Insira a nota da P3: ")))
    p4.append(float(input("Insira a nota da P4: ")))
    media.append((p1[i] + p2[i] + p3[i] + p4[i])/4)
    if (media[i] >= 7.0):
        aux = aux + 1
print("Nesta turma apenas", aux, "alunos estão com média maior que 7")



























#alun = int(input("Digite o número do aluno! "))
#print("A média do aluno é: ")


    
