from tkinter import * 
from tkinter import messagebox as mb
from tkinter import filedialog as fd

def exit():
    answer = mb.askyesno(title="", message="Вийти з програми?")
    if answer:
        root.destroy()
def save():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                    ("HTML files", "*.html;*.htm"),
                                    ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

def load():
    file_name = fd.askopenfilename(filetypes=(("TXT files", "*.txt"),
                                    ("HTML files", "*.html;*.htm"),
                                    ("All files", "*.*")))
    f = open(file_name)
    s = f.read()
    text.delete(1.0, END)
    text.insert(1.0, s)
    f.close()


root = Tk() 
m = Menu(root)
root.config(menu=m)
text = Text(bg="yellow")

mm_file = Menu(m)
m.add_cascade(label='File', menu=mm_file)
mm_file.add_command(label='New')
mm_file.add_command(label='Load', command=load)
mm_file.add_command(label='Save', command=save)
mm_file.add_command(label='Exit', command=exit)

mm_edit = Menu(m)
m.add_cascade(label='Edit', menu=mm_edit)
mm_edit.add_command(label='Copy')
mm_edit.add_command(label='Paste')

text.pack()

root.mainloop()
