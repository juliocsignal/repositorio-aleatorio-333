med = int(input("Olá, diga em qual a medida para a conversão! (C = 1 / F = 2)"))
value = int(input("Informe o valor a ser convertido! "))

if med == 1:
    print("Você está convertendo de C° para F°!")
    f = ((value/5)*9)+32
    print("O valor em F° é",f)
    

if med == 2:
    print("Você está convertendo de F° para C°")
    c = ((value - 32)/9)*5
    print("O valor em C° é",c)
