import tkinter

platnoDB=tkinter.Canvas(width=800, height=500, bg='white')
platnoDB.pack()

platnoDB.create_rectangle(190,180,210,600, fill="grey", outline="grey")
platnoDB.create_rectangle(200,200,500,400, fill="red", outline="red")

platnoDB.create_rectangle(275,200,325,400, fill="white", outline="white")
platnoDB.create_rectangle(200,275,500,325, fill="white", outline="white")

platnoDB.create_rectangle(285,200,315,400, fill="blue", outline="blue")
platnoDB.create_rectangle(200,285,500,315, fill="blue", outline="blue")

