from tkinter import *

root = Tk()
root.geometry('523x341+200+200')
label1 = Label(text="Курс", font='Arial 14', justify ='left')
label2 = Label(text="Гривні", font='Arial 14', justify='left')
label3 = Label(text="Євро", font='Arial 14', justify='left')
entry1 = Entry(font='Arial 14')
entry2 = Entry(font='Arial 14')
entry3 = Entry(font='Arial 14')
button1 = Button(text="грн в євро", font='Arial 14', width=12)
button2 = Button(text="євро в грн", font='Arial 14', width=12)
entry1.insert(0,'32.00')
entry2.insert(0,'0')
entry3.insert(0,'0')


label1.place(x=90, y=44)
label2.place(x=90, y=121)
label3.place(x=90, y=185)
entry1.place(x=208, y=44)
entry2.place(x=208, y=121)
entry3.place(x=208, y=185)
button1.place(x=150, y=281)
button2.place(x=300, y=281)

def funcGrnToEuro(x):
    print(x)
    k = float(entry1.get())
    g = float(entry2.get())
    e = g / k
    entry3.delete(0, END)
    entry3.insert(0, str(e))

def funcEuroToGrn(x):
    k = float(entry1.get())
    e = float(entry3.get())
    g = e * k
    entry2.delete(0,END)
    entry2.insert(0, str(g))


button1.bind('<Button-1>', funcGrnToEuro)
button2.bind('<Button-1>', funcEuroToGrn)

root.mainloop()