from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
def ex():
    answer = mb.askyesno(title="Вихід з програми", message="Ви хочете закрити?")
    if answer: root.destroy()
def op():
    answer = fd.askopenfilename()
    f = open(answer)
    s = f.read()
    text.delete(1.0, END)
    text.insert(1.0,s)
    f.close()
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
m_file.add_command(label='Open', command=op)
m_file.add_command(label='Save',command=sav)
m_file.add_command(label='Exit', command=ex)

m_edit = Menu(m)
m.add_cascade(label='Edit',menu=m_edit)
m_edit.add_command(label='Cut'                )
m_edit.add_command(label='Copy'                )
m_edit.add_command(label='Paste')

text = Text()
text.pack()
root.mainloop()
