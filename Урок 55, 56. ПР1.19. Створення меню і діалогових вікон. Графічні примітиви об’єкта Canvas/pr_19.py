from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
def ex():
    answer = mb.askyesno(title="Вихід з програми", message="Ви хочете закрити?")
    if answer: root.destroy()

def sav():
    answer = fd.asksaveasfilename()
    f = open(answer,'w')
    s = text.get(1.0,END)
    f.write(s)
    f.close()

root = Tk()
m = Menu(root)
root.geometry('400x300+100+100')
root.config(menu=m)

m_file = Menu(m)
m.add_cascade(label='File',menu=m_file)
m_file.add_command(label='Save',command=sav)
m_file.add_command(label='Exit', command=ex)

text = Text()
text.pack()
root.mainloop()
