from tkinter import *

root = Tk()
root.title = "My first window"

lbl = Label(root, text="Oppa")

ent = Entry(root, text="ssss")

def func(a):
    lbl['text'] = "dddddddddd"
    print(ent.get())


btn1 = Button(root, text="Ok", width=5, height=2, bg="red", fg="white", font="Arial 20")




btn1.bind('<Button-1>', func )


btn1.pack()

lbl.pack()
ent.pack()
root.mainloop()
