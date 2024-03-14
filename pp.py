from tkinter import Tk, Text, BOTH

def record(event):
    print('char = {}'.format(event.keysym))

root = Tk()
text = Text(root, width=20, height=5)
text.bind('<keyPress>', record)
text.pack(expand = True, fill = BOTH)
root.mainloop()

