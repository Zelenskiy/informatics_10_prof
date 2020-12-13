from tkinter import *

root = Tk()
root.geometry('523x341+200+200')

label1 = Label(text="Кількість", font='Arial 14', justify ='left')
label2 = Label(text="Ціна за одиницю", font='Arial 14', justify='left')
label3 = Label(text="Повна сума", font='Arial 14', justify='left')
entry1 = Entry(font='Arial 14')
entry2 = Entry(font='Arial 14')
entry3 = Entry(font='Arial 14')
button1 = Button(text="Обчислити", font='Arial 14', width=12)

entry1.insert(0,'0')
entry2.insert(0,'0.00')
entry3.insert(0,'0.00')

def calc(x):
    num = int(entry1.get())
    price = float(entry2.get())
    sum = num * price
    if num > 10:
        sum -= (num - 10)*0.2*price
    entry3.delete(0, END)
    entry3.insert(0, str(sum))

button1.bind('<Button-1>', calc)

label1.place(x=90, y=44)
label2.place(x=90, y=121)
label3.place(x=90, y=185)
entry1.place(x=248, y=44)
entry2.place(x=248, y=121)
entry3.place(x=248, y=185)
button1.place(x=330, y=281)


root.mainloop()
