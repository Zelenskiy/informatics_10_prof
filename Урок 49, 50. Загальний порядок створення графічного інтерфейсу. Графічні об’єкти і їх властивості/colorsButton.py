from tkinter import *

import random



 
def change ( ) :
    global n
    n+=1
    b1 [ 'text' ]  =  "Змінено" + str(n)
    b1 [ 'bg' ]  =  '#'+'{0:06X}'.format(random.randint(0,16777216)) 
    b1 [ 'activebackground' ]  =  '#555555' 
    b1 [ 'fg' ]  =  '#ffffff' 
    b1 [ 'activeforeground' ]  =  '#ffffff'
 

n=0
root = Tk ( ) 
b1 = Button ( text = "Змінити" ,  
            width = 15 , height = 3 ) 
b1. config ( command = change ) 
b1. pack ( ) 
root. mainloop ( )
