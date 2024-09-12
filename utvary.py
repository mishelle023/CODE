import tkinter

platnoDB=tkinter.Canvas(width=800, height=500, bg='white')
platnoDB.pack()

platnoDB.create_line(190,230,190,400, fill="black")
platnoDB.create_rectangle(250,200,400,400, fill="lightgreen", outline="lightgreen")
platnoDB.create_oval(170,300,210,230, fill="yellow", outline="lightyellow")

