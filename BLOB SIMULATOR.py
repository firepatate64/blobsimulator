##Imports
from tkinter import*
import random

##Variables
list = []
for i in range(50):
    list.append([0]*50)
aleatoir = 1

##Fonctions
def point(x,y):
    list[x][y] = 1
def blob(x,y,i):
    global aleatoir
    if(x<50 and y<50 and x>0 and y>0):
        if (i<100 and list[x][y]==0):
            if(random.randint(0,aleatoir)==0 or i<1):
                root.after(100, lambda : blob(x+1,y,i+1))
            if(random.randint(0,aleatoir)==0 or i<1):
                root.after(100, lambda : blob(x-1,y,i+1))
            if(random.randint(0,aleatoir)==0 or i<1):
                root.after(100, lambda : blob(x,y+1,i+1))
            if(random.randint(0,aleatoir)==0 or i<1):
                root.after(100, lambda : blob(x,y-1,i+1))
        point(x,y)
def grille(window, canvas):
    width = 800
    height = 600
    canvas.delete(['all'])

    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
    index1 = 0
    index2 = 0
    for i in list:
        for ib in i:
            if(ib):
                x = index1
                y = index2-index1*50
                canvas.create_rectangle(x*10,y*10,x*10+10,y*10+10,fill = "blue")
            index2 = index2+1
        index1 = index1+1
    root.after(100, lambda : grille(root,canvas))

def lancerleblob(a,b,c,d,e):
    grille(a,b)
    blob(c,d,e)

##Main
root = Tk()
canvas = Canvas(root, background='white', width=800, height=600)
width = 800
height = 600
for line in range(0, width, 10): # range(start, stop, step)
    canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

for line in range(0, height, 10):
    canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
canvas.pack()
bouton=Button(root, text="Lancer le BLOB",  command=lambda : lancerleblob(root,canvas,25,25,0))
bouton.pack()
bouton1=Button(root, text="Fermer", command=root.destroy)
bouton1.pack()
root.mainloop()
