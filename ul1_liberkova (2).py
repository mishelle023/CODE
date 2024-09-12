import turtle, random
x=random.randint(100,200)
y=random.randint(80,200)
medzera=5
turtle.speed(10)

for i in range(6):
    if x>medzera:
        turtle.penup()
        turtle.goto(x, -y/2)
        turtle.pendown()
        turtle.goto(x, y/2)
        turtle.penup()
        turtle.goto(-x, y/2)
        turtle.pendown()
        turtle.goto(-x, -y/2)
        medzera=medzera+random.randint(1,3)
        x=x-medzera


turtle.mainloop()
