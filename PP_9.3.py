from tkinter import Tk, Button, LEFT, RIGHT
from tkinter.messagebox import showinfo
from time import strftime, localtime, gmtime

def hl():
    'exibe informação de dia e hora'
    horaL = strftime('Hora local\nDia: %d %b %y\nHora: %H:%M:%S: %p\n', localtime())
    showinfo(message=horaL)

def hg():
    horaG = strftime('Hora Greenwich\nDia: %d %b %y\nHora: %H:%M:%S: %p\n', gmtime())
    showinfo(message=horaG)

root = Tk()
button1 = Button(root, text='Hora local', command=hl)
button1.pack(side=RIGHT)
button2 = Button(root, text='Hora Greenwich', command=hg)
button2.pack(side=LEFT)
root.mainloop()