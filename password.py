import tkinter



class LetsPlay(tkinter.Tk):

    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.configure(background='white')
        self.grid()
        
        self.lblA = tkinter.Label(text="Login: ")
        self.lblA.grid(column=0, row=0)
        self.lblA.configure(background='white')
        

        self.lblB = tkinter.Label(text="Senha: ")
        self.lblB.grid(column=0, row=1)
        self.lblB.configure(background='white')


        self.entryA = tkinter.Entry(self)
        self.entryA.grid(column = 1, row = 0)

        self.entryB = tkinter.Entry(self)
        self.entryB.grid(column = 1, row = 1)
        self.entryB.config(show="*")

        self.butt = tkinter.Button(self, text="Entrar",command=self.OnClick,bg="#15a25e")
        self.butt.grid(column=1,row=2)

        self.butt = tkinter.Button(self, text="Parar",command=self.StopButton,bg="Red")
        self.butt.grid(column=2,row=2)

    def OnClick(self):
        nome = str(self.entryA.get())
        senha = str(self.entryB.get())
        nome = nome + "\n"
        senha = senha + "\n" + "\n"

        arq = open('lista.txt', 'w')
        arq.write(nome)
        arq.write(senha)

    def StopButton(self):
        arq.close()
        

app = LetsPlay(None)      #criamos uma aplicação sem nenhum pai, pois é a principal.
app.title('Login')    #especificamos o título de nossa aplicação
app.mainloop()
