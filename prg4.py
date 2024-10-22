import tkinter
import random

p=tkinter.Canvas(width=800, height=500, bg="white")
p.pack()

for i in range(500):
    x=random.randrange(800)
    y=random.randrange(500)
    if  x>400:
        p.create_line(400,250,x,y, fill="red")
    else:
        p.create_line(400,250,x,y, fill="blue")

p.mainloop()
