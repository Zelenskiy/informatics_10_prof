from tkinter import *
 
root = Tk()
e1 = Entry(width=50)
 
 
def insert():
    e1.insert(0, "Tkinter - GUI ")
    print(e1.get())
 
 
but = Button(text="Вставити", command=insert, height=5)
e1.pack()
but.pack()
root.mainloop()
