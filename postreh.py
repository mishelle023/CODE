import tkinter
import random

canvas = tkinter.Canvas(width=500, height=700)
canvas.pack()

stvorec=canvas.create_rectangle(100,100,200,200, fill="red")
pozicia= ({event.x}, {event.y})
def kruh00(event):
    global stvorec
    canvas.delete(stvorec)
    x=random.randrange(100,500)
    y=random.randrange(100,500)
    stvorec=canvas.create_rectangle(x,y,x+100,y+100, fill="red")


canvas.bind("<Button-1>", kruh00)


