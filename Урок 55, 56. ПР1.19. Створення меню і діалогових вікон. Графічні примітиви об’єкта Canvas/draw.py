from tkinter import *

def move(e):
    pos = cnv.coords(kv)
    x = e.x - pos[0]
    y = e.y - pos[1]
    cnv.move(kv,x,y)

root = Tk()
root.geometry('600x500+200+100')
cnv = Canvas(width=600, height=500)
cnv.pack()
kv = cnv.create_rectangle(50,50,150,150,fill="red")
tr = cnv.create_polygon([170,100], [150,130], [220,200], fill="blue")
el=cnv.create_oval([200,200], [250,350],fill="green")

cnv.bind('<B1-Motion>', move)
# cnv.bind('<Button-1>', move)
root.mainloop()