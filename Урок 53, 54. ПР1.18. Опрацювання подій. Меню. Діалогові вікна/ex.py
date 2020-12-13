from tkinter import * 
from tkinter import messagebox as mb

def exit():
    answer = mb.askyesno(title="", message="Вийти з програми?")
    if answer:
        root.destroy()


root = Tk() 
m = Menu(root)
root.config(menu=m)
text = Text(bg="yellow")

mm_file = Menu(m)
m.add_cascade(label='File', menu=mm_file)
mm_file.add_command(label='New')
mm_file.add_command(label='Load')
mm_file.add_command(label='Save')
# mm_file.add_command(label='Exit', command=lambda : root.destroy())
mm_file.add_command(label='Exit', command=exit)

mm_edit = Menu(m)
m.add_cascade(label='Edit', menu=mm_edit)
mm_edit.add_command(label='Copy')
mm_edit.add_command(label='Paste')

text.pack()

root.mainloop()
