import turtle
k=turtle.Turtle()

def V():
    for i in range(4):
        k.forward(100)
        k.right(90)

k.forward(50)
k.right(90)
k.penup()
k.forward(25)
k.pendown()
k.forward(40)
k.penup()
k.right(90)
k.forward(30)
k.right(90)
k.forward(25)
k.pendown()
k.right(30)

def T():
    for i in range(3):
        k.forward(15)
        k.right(120)

T()
k.penup()
k.right(60)
k.forward(45)
k.pendown()
k.left(60)
T()
k.right(60)
k.penup()
k.forward(7.5)
k.right(90)
k.penup()
k.forward(25)
k.pendown()

for i in range(40):
    k.forward(2)
    k.right(5)
