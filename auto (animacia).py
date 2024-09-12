import tkinter

canvas = tkinter.Canvas(width=600, bg="light blue")
canvas.pack()

canvas.create_line(0,250, 600, 250, fill="grey", width=100)
canvas.create_oval(-20, -20, 110, 100, fill="yellow", outline="yellow")



def klik(event):
    p=30
    o=20
    c=30
    for i in range(3):

        canvas.create_oval(event.x, event.y, event.x+50, event.y+50, fill="white", outline="white")
        event.x=event.x+p
    event.x=event.x-3*p
    event.x=event.x+10
    event.y=event.y-o
    for i in range(2):

        canvas.create_oval(event.x, event.y, event.x+50, event.y+50, fill="white", outline="white")
        event.x=event.x+c




canvas.bind('<Button-1>', klik)


auto1 = canvas.create_line(290,150, 150, 150, fill="red", width=50)
auto2 = canvas.create_oval(200, 200, 130, 140, fill="black")
auto3 = canvas.create_oval(300, 200, 230, 140, fill="black")
auto4 = canvas.create_line(190,110, 250, 110, fill="red", width=40)
canvas.update()
canvas.after(1000)

for i in range(80):

    canvas.move(auto1, 3, 0)
    canvas.move(auto2, 3, 0)
    canvas.move(auto3, 3, 0)
    canvas.move(auto4, 3, 0)
    canvas.update()
    canvas.after(30)
