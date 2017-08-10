from funcoes import *
import tkinter

class minhaApp_tk(tkinter.Tk):
    def __init__(self,parent):

        tkinter.Tk.__init__(self, parent)

        self.parent = parent

        self.initialize()

    def initialize(self):
        self.entryN = tkinter.Entry(self)
        self.entryN.grid(column=0, row=1, sticky='EW')    

        self.entryP = tkinter.Entry(self)
        self.entryP.grid(column=2, row=1, sticky='EW')
        
        self.lblN = tkinter.Label(self, text="Qual é o conjunto?")
        self.lblN.grid(column=0, row=2)

        self.lblP = tkinter.Label(self, text="Qual é a parte?")
        self.lblP.grid(column=2, row=2)

        self.btnCalcula = tkinter.Button(self, text="CALCULAR", command=self.OnButtonCalcClick)
        self.btnCalcula.grid(column=10, row=1)

        self.lblC = tkinter.Entry(self)
        self.lblC.grid(column=12, row=1)

    def OnButtonCalcClick(self):
        n = int(self.entryN.get())
        p = int(self.entryP.get())

        resp = int(Combina(n,p))

        self.lblC.delete(0, tkinter.END)
        self.lblC.insert(0, str(resp))


if __name__ == "__main__":
    app = minhaApp_tk(None)  # criamos uma aplicação sem nenhum pai, pois é a principal.
    app.title('Equação do Segundo Grau!')  # especificamos o título de nossa aplicação
    app.mainloop()




