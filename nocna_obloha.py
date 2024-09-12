import tkinter

platnoAK=tkinter.Canvas(width=2000, height=1000, bg="darkblue")
platnoAK.pack()

platnoAK.create_oval(120,120,300,300, fill="yellow", outline="yellow")
platnoAK.create_oval(190,160,310,280, fill="darkblue", outline="darkblue")

platnoAK.create_text(1000,500, text="NOC", fill="red", angle=180, font="arial 60 bold")
platnoAK.create_text(80,900, text="Adela Kučerová, sexta, 25.10", fill="white")

platnoAK.create_oval(1200,700,1220,720, fill="white", outline="white")
platnoAK.create_oval(1400,400,1420,420, fill="white", outline="white")
platnoAK.create_oval(900,300,920,320, fill="white", outline="white")
platnoAK.create_oval(1500,600,1520,620, fill="white", outline="white")
platnoAK.create_oval(1300,500,1320,520, fill="white", outline="white")
platnoAK.create_oval(400,700,420,720, fill="white", outline="white")
platnoAK.create_oval(300,900,320,920, fill="white", outline="white")
platnoAK.create_oval(100,400,120,420, fill="white", outline="white")
platnoAK.create_oval(1700,200,1720,220, fill="white", outline="white")
platnoAK.create_oval(600,400,620,420, fill="white", outline="white")