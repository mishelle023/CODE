import tkinter, random

p=tkinter.Canvas(width=800, height=500, bg='white')
p.pack()

obr_vcela= tkinter.PhotoImage(file="vcela.gif")
vcela=p.create_image(50,30, image=obr_vcela)

obr_kvet= tkinter.PhotoImage(file="kvet.gif")
kvet1=p.create_image(250,50, image=obr_kvet)
kvet2=p.create_image(230,350, image=obr_kvet)
kvet3=p.create_image(360,180, image=obr_kvet)
kvet4=p.create_image(430,150, image=obr_kvet)
kvet5=p.create_image(180,250, image=obr_kvet)

obr_ul= tkinter.PhotoImage(file="ul.gif")
ul=p.create_image(30,30, image=obr_ul)



pozicia=[[250,50], [230,350], [360,180], [430,150], [180,250]]
random.shuffle(pozicia)
for prvok in pozicia:
    p.move(vcela, prvok[0], prvok[1])
    p.update()
    p.after(2000)
    p.move(vcela, -prvok[0], -prvok[1])
    p.update()
    p.after(2000)
