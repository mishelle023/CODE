import tkinter

platnoDZ=tkinter.Canvas( width=10000, heigh=1000, bg="white")
platnoDZ.pack()

platnoDZ.create_rectangle(50,300,500,400, fill="black", outline="black")
platnoDZ.create_rectangle(50,400,500,500, fill="red", outline="red")
platnoDZ.create_rectangle(50,500,500,600, fill="yellow", outline="yellow")

platnoDZ.create_line(275,400,275,600, fill="white", width=100)
