from tkinter import Tk, Button, Entry, Label, END
from time import strptime, strftime

def mostra():
    global dataEnt
    data = dataEnt.get()
    diasemana = strftime('%A', strptime(data, '%b %d %y'))
    data.insert(0, diasemana+' ')

def apaga():
    global dataEnt
    dataEnt.delete(0, END)

root = Tk()

label = Label(root, text='Digite a Data')
label.grid(row=0, column=0)

dataEnt = Entry(root)
dataEnt.grid(row=0, column=1)

button1 = Button(root, text='Entrar', command=mostra)
button1.grid(row=1, column=0)

button2 = Button(root, text='Apagar', command=apaga)
button2.grid(row=1, column=1)
root.mainloop()