#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

#opa mudei

class minhaApp_tk(tkinter.Tk):
    def __init__ (self,parent):

        tkinter.Tk.__init__(self,parent)

        self.parent = parent

        self.initialize()


    def initialize(self):
        self.grid()

    #Descriçao da Equação
        self.lblEq = tkinter.Label(self, text="x²")
        self.lblEq.grid(column=1,row=1)
        self.lblEq1 = tkinter.Label(self, text="x")
        self.lblEq1.grid(column=3,row=1)
        self.lblTot = tkinter.Label(self, text="O resultado é: ")
        self.lblTot.grid(column=6,row=0)

    #Coeficiente A
        self.lblA= tkinter.Label(self, text="Coeficiente A")
        self.lblA.grid(column=0, row=2)

    #Coeficiente B
    
        self.lblB= tkinter.Label(self, text="Coeficiente B")
        self.lblB.grid(column=2, row=2)

    #Coeficiente C

        self.lblC= tkinter.Label(self, text="Coeficiente C")
        self.lblC.grid(column=4, row=2)

    #Raizes
        #x1
    
        self.lblRes = tkinter.Label(self, text="X'")
        self.lblRes.grid(column=6, row =2)

        self.entryRes = tkinter.Entry(self)
        self.entryRes.grid(column=6, row=1)

        #x2

        self.lblResB = tkinter.Label(self, text="X''")
        self.lblResB.grid(column=8, row =2)

        self.entryResB = tkinter.Entry(self)
        self.entryResB.grid(column=8, row=1)


    #Entrada dos coeficientes

    #Coef. A
    
        self.entryA = tkinter.Entry(self)
        self.entryA.grid(column=0,row=1,sticky='EW')

    #Coef. B
    
        self.entryB = tkinter.Entry(self)
        self.entryB.grid(column=2,row=1,sticky='EW')

    #Coef. C
    
        self.entryC = tkinter.Entry(self)
        self.entryC.grid(column=4,row=1,sticky='EW')

    #Criação do Botão "Calcular"

        self.btnCalcula = tkinter.Button(self,text="CALCULAR", command= self.OnButtonCalcClick)
        self.btnCalcula.grid(column=10,row=1)

    
    def OnButtonCalcClick(self):

        #Entrada dos coeficientes

        a = float(self.entryA.get())
        b = float(self.entryB.get())
        c = float(self.entryC.get())

        #Descrição da função
           
        #Cálculo das raízes
        
        delta = b**2 - (4*a*c)

        if (a != 0):
            if (delta < 0):
                self.entryRes.delete(0,tkinter.END)
                self.entryRes.insert(0,"Não possui raízes reais!")
                self.entryResB.delete(0,tkinter.END)


            if (delta > 0):
                x1 = (-b +(delta**0.5))/(2*a)
                x2 = (-b -(delta**0.5))/(2*a)
                x1 = round(x1,2)
                x2 = round(x2,2)
                self.entryRes.delete(0,tkinter.END)
                self.entryRes.insert(0,str(x1))
                self.entryResB.delete(0,tkinter.END)
                self.entryResB.insert(0,str(x2))
            if (delta == 0):
                x1 = (-b +(delta**0.5))/(2*a)
                x1 = round(x1,2)
                self.entryRes.delete(0,tkinter.END)
                self.entryRes.insert(0,str(x1))
                self.entryResB.delete(0,tkinter.END)
                self.entryResB.insert(0,"Raíz única! ")
        else:
            self.entryRes.delete(0,tkinter.END)
            self.entryRes.insert(0,"Não é de 2º Grau! ")
            self.entryResB.delete(0,tkinter.END)
            self.entryResB.insert(0,"Seu ANIMAL!")
            
if __name__ == "__main__":
    app = minhaApp_tk(None)      #criamos uma aplicação sem nenhum pai, pois é a principal.
    app.title('Equação do Segundo Grau!')    #especificamos o título de nossa aplicação
    app.mainloop()
    
