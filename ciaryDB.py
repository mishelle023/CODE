import turtle
import random
x = random.randint(100, 200)
medzera = 5
dlzka= random.randint(80, 200)

turtle.speed(5)

for i in range(6):

    if x > medzera:

        turtle.penup()
        turtle.goto(x, -dlzka/2)
        turtle.pendown()
        turtle.goto(x, dlzka/2)
        turtle.penup()
        turtle.goto(-x, -dlzka/2)
        turtle.pendown()
        turtle.goto(-x, dlzka/2)
        medzera=medzera+ random.randint(1,3)
        x=x-medzera


turtle.mainloop()