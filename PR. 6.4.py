import tkinter
c = tkinter.Canvas(width= 300, height=300)
c.pack()

def kresli(p,v,m):
    x,y =10,10
    for i in range(1, p+1):
        for j in range (1, i+1):
            c.create_oval(x-v,y-v,x+v,y+v,fill="gold")
            x += (2*v +m)
        y += (2*v + m)
    x = 10

pocet= int(input('počet bodiek: '))
velkost = int(input('velkost bodiek: '))
medzera= int(input('medzera: '))

kresli(pocet,velkost,medzera)

c.mainloop()