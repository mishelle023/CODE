import tkinter

p= tkinter.Canvas(width= 1500, height= 1500, bg="white")

p.pack()


#Nórska vlajka
p.create_rectangle(200,500,700,200, fill="red", outline="red")
p.create_line(350,510,350,190, fill="white", width=60)
p.create_line(190,350,710,350, fill="white", width=60)
p.create_line(350,500,350,200, fill="darkblue", width=30)
p.create_line(200,350,700,350, fill="darkblue", width=30)


#Grécka vlajka
p.create_rectangle(800,500,1300,200, fill="darkblue", outline="darkblue")
p.create_line(800,251,1310,251, fill="white", width=40)
p.create_line(800,326,1310,326, fill="white", width=40)
p.create_line(800,401,1310,401, fill="white", width=40)
p.create_line(800,460,1310,460, fill="white", width=40)
p.create_rectangle(800,380,1000,200, fill="darkblue", outline="darkblue")
p.create_line(900,380,900,200, fill="white", width=30)
p.create_line(800,290,1000,290, fill="white", width=30)
