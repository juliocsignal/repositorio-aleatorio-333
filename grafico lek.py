#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
import numpy as np
import matplotlib.pyplot as plt

a = []


#INICIO

a = float(input("Digite o primeiro coeficiente!"))
b = float(input("Digite o segundo coeficiente!"))
c = float(input("Digite o terceiro coeficiente!"))
        

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

#FIM

#m = int(input("Result"))

m = 15

e = a * (m * m) + b * m + c


plt.plot([x1,x2])
plt.title("Muito Fácil")
plt.show()
