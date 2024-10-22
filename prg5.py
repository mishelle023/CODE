import tkinter
import random
pocet=0
pocet1=0

p=tkinter.Canvas(width=800, height=500, bg="white")
p.pack()

for i in range(1000):
    x=random.randrange(800)
    y=random.randrange(500)
    if  x>400:
        p.create_line(400,250,x,y, fill="blue")
        pocet1=pocet1+1
    else:
        p.create_line(400,250,x,y, fill="red")
        pocet=pocet+1


print("Počet červených lúčov je", pocet, ".")
print("Počet modrých čiar je", pocet1, ".")

p.mainloop()