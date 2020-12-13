from tkinter import *

def grnToEuro(e):
    g = float(e2.get())
    k = float(e1.get())
    eu = g / k
    e3.delete(0, END)
    e3.insert(0, str(eu))


def euroToGrn(e):
    eu = float(e3.get())
    k = float(e1.get())
    g = eu * k
    e2.delete(0, END)
    e2.insert(0, str(g))


root = Tk()
root.geometry('376x216+100+80')
l1 = Label(text='Курс (грн за євро)')
e1 = Entry(width=25)
e1.insert(0,'33.00')
l2 = Label(text='Гривні')
e2 = Entry(width=25)
e2.insert(0,'0.00')
l3 = Label(text='Євро')
e3 = Entry(width=25)
e3.insert(0,'0.00')
b1 = Button(text='грн в євро', width=18, height=1)
b2 = Button(text='євро в грн', width=18, height=1)
b1.bind('<Button-1>', grnToEuro)
b2.bind('<Button-1>', euroToGrn)

l1.place(x=48, y=28)
e1.place(x=188, y=28)
l2.place(x=48, y=74)
e2.place(x=188, y=74)
l3.place(x=48, y=120)
e3.place(x=188, y=120)
b1.place(x=58, y=176)
b2.place(x=200, y=176)

root.mainloop()
