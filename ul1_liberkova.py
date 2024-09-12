import turtle, random
x=random.randint(100,200)
y=random.randint(80,200)

turtle.speed(10)

for i in range(6):
    turtle.penup()
    turtle.goto(x, -y/2)
    turtle.pendown()
    turtle.goto(x, y/2)

    turtle.penup()
    turtle.goto(-x, y/2)
    turtle.pendown()
    turtle.goto(-x, -y/2)
    x=x+10+random.randint(1,3)

turtle.mainloop()
