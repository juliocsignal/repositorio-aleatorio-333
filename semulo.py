a = []
impar = []
par = []

for i in range(3):
    a.append(int(input()))
    if ((a[i] % 2) == 1 ):
        impar.append(a[i])
    if ((a[i] % 2) == 0):
        par.append(a[i])

        
print ("Números inseridos: ",a)
print("Números pares: ", par)
print("Números ímpares: ", impar)

b = input()
