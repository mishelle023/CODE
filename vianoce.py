import tkinter

p=tkinter.Canvas(width=1500, height=800, bg="white")

p.pack()

#stromček
p.create_polygon(500,700,650,500,800,700, fill="green", outline="green")
p.create_polygon(500,600,650,400,800,600, fill="green", outline="green")
p.create_polygon(500,500,650,300,800,500, fill="green", outline="green")
p.create_rectangle(625,700,675,900, fill="brown", outline="brown")

#ozdoby
p.create_oval(550,670,570,650, fill="red", outline="red")
p.create_oval(720,670,740,650, fill="blue", outline="blue")
p.create_oval(640,650,660,630, fill="yellow", outline="yellow")
p.create_oval(550,470,570,450, fill="pink", outline="pink")
p.create_oval(630,450,650,430, fill="orange", outline="orange")
p.create_oval(730,470,750,450, fill="lightblue", outline="lightblue")
p.create_oval(550,570,570,550, fill="blue", outline="blue")
p.create_oval(730,570,750,550, fill="purple", outline="purple")
p.create_oval(630,370,650,350, fill="red", outline="red")
p.create_oval(670,530,690,550, fill="red", outline="red")

#darčeky
p.create_rectangle(720,750,770,800, fill="red", outline="red")
p.create_rectangle(480,750,570,800, fill="lightgreen", outline="lightgreen")
p.create_rectangle(820,750,870,800, fill="blue", outline="blue")
p.create_line(745,750,745,800, fill="yellow", width=10)
p.create_line(720,775,770,775, fill="yellow", width=10)
p.create_line(480,775,570,775, fill="purple", width=10)
p.create_line(525,750,525,800, fill="purple", width=10)
p.create_line(820,775,871,775, fill="orange", width=10)
p.create_line(845,750,845,800, fill="orange", width=10)
