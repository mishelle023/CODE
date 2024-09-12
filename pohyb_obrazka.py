import tkinter

canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()

obr = tkinter.PhotoImage(file='vcela.png')
obr_id = canvas.create_image(100, 400, image=obr)



k1 = tkinter.PhotoImage(file='kvet.png')
k1_id = canvas.create_image(100, 500, image=obr)
k2 = tkinter.PhotoImage(file='kvet.png')
k2_id = canvas.create_image(100, 300, image=obr)
k3 = tkinter.PhotoImage(file='kvet.png')
k3_id = canvas.create_image(200, 400, image=obr)
k4 = tkinter.PhotoImage(file='kvet.png')
l4_id = canvas.create_image(0, 400, image=obr)




canvas.update()
canvas.after(1000)
canvas.delete(obr_id)

