import tkinter

class Registro(tkinter.Tk):
    def __init__ (self,parent):

        tkinter.Tk.__init__(self,parent)
        
        self.parent = parent

        self.initialize()


    def initialize(self):
        self.grid()

        #Declarando as variáveis a serem usadas
        
        

        #Criação dos campos

        self.lblName = tkinter.Label(self,text=" Título da conta: ")
        self.lblName.grid(column=0,row=0)

        self.lblConta = tkinter.Label(self,text="Valor da conta: ")
        self.lblConta.grid(column=0,row=1)

        self.entryName = tkinter.Entry(self)
        self.entryName.grid(column=1,row=0)

        self.entryConta = tkinter.Entry(self)
        self.entryConta.grid(column=1,row=1)

        self.entryStart = tkinter.Button(self,text="Próxima",command=self.CalcMes)
        self.entryStart.grid(column=2,row=0)

        self.entryStop = tkinter.Button(self,text="Parar")
        self.entryStop.grid(column=2,row=1)

        
    def CalcMes(self):
        soma = "0"
        contas = []
        nomec = []
        cont = 0

        nomec.append(self.entryName.get())
        contas.append(int(self.entryConta.get()))
        cont = cont + 1

        for i in range(cont):
            print(nomec[i],":",contas[i])
            result = sum(contas)
        print("O somatório das contas é igual a:",result)


app = Registro(None)      
app.title('Contas do Mês')
app.geometry("500x400")
app.mainloop()
