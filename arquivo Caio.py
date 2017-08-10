from tkinter import *

def changeCol():
    butt["bg"]="#FF00DE"
    butt["text"]="ARRAZOU VIADO!"
    return

root = Tk()

root.geometry("1000x800")

lab1 = Label(root, text="Coé RAPAZIADA!")

butt = Button(root, text="SAI DO ARMÁRIO!", bg="#87A1FF", command=changeCol)

lab1.pack()
butt.pack()


root.mainloop()

