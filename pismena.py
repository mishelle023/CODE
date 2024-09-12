import tkinter

p=tkinter.Canvas(width=600, height=300, bg="black")

p.pack()

p.create_polygon(125,250,50,50,100,50,125,130,150,50,200,50, outline="yellow")
p.create_line(400,75,550,75, fill="purple", width=50)
p.create_line(475,75,475,250, fill="purple", width=50)
p.create_line(405,75,545,75, fill="pink", width=40)
p.create_line(475,75,475,245, fill="pink", width=40)
p.create_line(250,50,250,250, fill="darkblue", width=40)
p.create_line(250,230,370,230, fill="darkblue", width=40)
p.create_line(250,55,250,245, fill="blue", width=30)
p.create_line(250,230,365,230, fill="blue", width=30)
