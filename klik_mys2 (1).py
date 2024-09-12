import tkinter as tk

def kruh00(event):
    canvas.delete(kruh)

def kruh01(event):
    canvas.delete(kruh1)

def kruh02(event):
    canvas.delete(kruh2)

def kruh03(event):
    canvas.delete(kruh3)

def kruh04(event):
    canvas.delete(kruh4)

canvas = tk.Canvas(width=500, height=700)
canvas.pack()
kruh=canvas.create_oval(120,180,270,300, fill="red")
kruh1=canvas.create_oval(220,280,340,400, fill="red")
kruh2=canvas.create_oval(20,80,140,200, fill="red")
kruh3=canvas.create_oval(320,380,440,500, fill="red")
kruh4=canvas.create_oval(400,450,540,550, fill="red")

canvas.bind("<Button-1>", kruh00)
canvas.bind("<Button-1>", kruh01)
canvas.bind("<Button-1>", kruh02)
canvas.bind("<Button-1>", kruh03)
canvas.bind("<Button-1>", kruh04)


