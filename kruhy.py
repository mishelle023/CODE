import random,tkinter
p=tkinter.Canvas(width=500, height=800, bg="white")
p.pack()




for i in range(40):
    x=random.randrange(500)
    y=random.randrange(800)
    a=random.randrange(90)
    if a<50:
        p.create_oval(x,y,x+a,y+a, fill="red")
    else:
        p.create_oval(x,y,x+a,y+a, fill="blue")

