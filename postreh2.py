import tkinter
import random

canvas = tkinter.Canvas(width=500, height=700)
canvas.pack()

x=random.randrange(100,500)
y=random.randrange(100,500)
kruh=canvas.create_rectangle(x,y,x+100,y+100, fill="red")

def kruh00(event):
    global kruh, x, y
    print(f"Myš sa pohybuje na pozícii ({event.x}, {event.y})")
    if x+100>event.x>x and y+100>event.y>y:
        x=random.randrange(100,500)
        y=random.randrange(100,500)
        canvas.delete(kruh)
        kruh=canvas.create_rectangle(x,y,x+100,y+100, fill="red")



canvas.bind("<Button-1>", kruh00)

