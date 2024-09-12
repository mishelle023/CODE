import turtle
import random

CURRENT_X: int = random.randint(100, 200)
X_SUBTRACTION: int = 5
LINE_LENGTH: int = random.randint(80, 200)

turtle.speed(9999)


def draw_line_from(x_from: int):
    turtle.penup()
    turtle.goto(x_from, -LINE_LENGTH)
    turtle.pendown()
    turtle.goto(x_from, LINE_LENGTH)


while CURRENT_X > 0:
    draw_line_from(CURRENT_X)
    draw_line_from(-CURRENT_X)

    CURRENT_X -= X_SUBTRACTION
    X_SUBTRACTION += random.randint(1, 3)

turtle.mainloop()
