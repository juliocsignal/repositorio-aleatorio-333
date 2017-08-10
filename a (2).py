import pecas
from pecas import *
casa = [0] * 64
A = [0] * 8
B = [0] * 8
C = [0] * 8
D = [0] * 8
E = [0] * 8
F = [0] * 8
G = [0] * 8
H = [0] * 8
 


for i in range(64):
    casa[i] = i + 1

for i in range(8):
    A[i] = "A" + str(i)

for i in range(8):
    B[i] = "B" + str(i)

for i in range(8):
    C[i] = "C" + str(i)

for i in range(8):
    D[i] = "D" + str(i)

for i in range(8):
    E[i] = "E" + str(i)

for i in range(8):
    F[i] = "F" + str(i)

for i in range(8):
    G[i] = "G" + str(i)

for i in range(8):
    H[i] = "H" + str(i)

def AcheCasa():  
    b = int(input("Informe a casa! "))
    
    if (b <= 7):
        print("Esta posição pertence a coluna 'A'")
        print(A[b])
        
    if (b <= 15 and b > 7):
        print("Esta posição pertence a coluna 'B'")
        print(B[b])

    if (b <= 23 and b > 15):
        print("Esta posição pertence a coluna 'C'")
        print(C[b - 15])

    if (b <= 31 and b > 23):
        print("Esta posição pertence a coluna 'D'")
        print(D[b - 23])

    if (b <= 39 and b > 31):
        print("Esta posição pertence a coluna 'E'")
        print(E[b])

    if (b <= 47 and b > 39):
        print("Esta posição pertence a coluna 'F'")
        print(F[b - 39])

    if (b <= 55 and b > 47):
        print("Esta posição pertence a coluna 'G'")
        print(G[b - 47])

    if (b <= 63 and b > 55):
        print("Esta posição pertence a coluna 'H'")
        print(H[b - 55])

def cavalo():
    entrada = input("Informe a casa! ")
    
    if (entrada[0] == "A"):
        print("Esta posição pertence a coluna 'A'")
        A[int(entrada[1])] = "CAVALO ESQ."
        print(A[int(entrada[1])])

        
    if (entrada[0] == "B"):
        print("Esta posição pertence a coluna 'B'")
        B[int(entrada[1])] = "CAVALO ESQ."
        print(B[int(entrada[1])])

        
    if (entrada[0] == "C"):
        print("Esta posição pertence a coluna 'C'")
        C[int(entrada[1])] = "CAVALO ESQ."
        print(C[int(entrada[1])])

        
    if (entrada[0] == "D"):
        print("Esta posição pertence a coluna 'D'")
        D[int(entrada[1])] = "CAVALO ESQ."
        print(D[int(entrada[1])])

        
    if (entrada[0] == "E"):
        print("Esta posição pertence a coluna 'A'")
        E[int(entrada[1])] = "CAVALO ESQ."
        print(E[int(entrada[1])])
        

    if (entrada[0] == "F"):
        print("Esta posição pertence a coluna 'A'")
        F[int(entrada[1])] = "CAVALO ESQ."
        print(F[int(entrada[1])])
        

    if (entrada[0] == "G"):
        print("Esta posição pertence a coluna 'A'")
        G[int(entrada[1])] = "CAVALO ESQ."
        print(G[int(entrada[1])])

    
    if (entrada[0] == "H"):
        print("Esta posição pertence a coluna 'A'")
        H[int(entrada[1])] = "CAVALO ESQ."
        print(H[int(entrada[1])])

        
cavalo()

#AcheCasa()

#def consulta(encontrar):
    #for i in range(64):
        #if (casa[i] == encontrar):
            #print("Casa",casa[i],"encontrada!")
            #break


