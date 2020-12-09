from tkinter import *

root = Tk()
root.geometry('600x400+200+100')
root.title = "My first window"

lbl = Label(root, text="Oppa")

ent = Entry(root, text="ssss")

def func(a):
    lbl['text'] = "dddddddddd"
    print(ent.get())


btn1 = Button(root, text="Ok", width=5, height=2, bg="red", fg="white", font="Arial 12")




btn1.bind('<Button-1>', func)


btn1.place(x=0, y=0)
# btn1.pack()
lbl.pack()
ent.pack()
root.mainloop()
