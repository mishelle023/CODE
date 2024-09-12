import tkinter

platnoDZ=tkinter.Canvas(width=2000, heigh=1000, bg="white")
platnoDZ.pack()

platnoDZ.create_rectangle(950,700,1050,850, fill="brown", outline="brown")
platnoDZ.create_polygon(1000,100,700,700,1300,700, fill="green", outline="green")
platnoDZ.create_polygon(1000,100,750,500,1250,500, fill="green", outline="green")
platnoDZ.create_polygon(1000,100,800,350,1200,350, fill="green", outline="green")
platnoDZ.create_oval(975,200,1025,250, fill="red")
platnoDZ.create_oval(975,300,1025,350, fill="red")
platnoDZ.create_oval(975,400,1025,450, fill="red")
platnoDZ.create_oval(975,500,1025,550, fill="red")
platnoDZ.create_oval(975,600,1025,650, fill="red")

platnoDZ.create_text(500,200,text="VIANOCE", fill="blue", font="arial 30 bold", angle=50)
