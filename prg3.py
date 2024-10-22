import tkinter
import random

p=tkinter.Canvas(width=800, height=500, bg="white")
p.pack()


for i in range(1000):
    f=random.choice(("red","blue","green"))
    x=random.randrange(800)
    y=random.randrange(500)
    p.create_line(400,250,x,y, fill=f)
p.mainloop()