a=[]

for i in range(5):
	aux = int(input("Digite um número: "))
	a.append(aux)

print(a)
print(len(a))
a.pop(-1)
print(len(a))
print(a)
print(max(a))
print(min(a))
