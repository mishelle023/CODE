from math import sqrt
import tkinter
c= tkinter.Canvas(width=320, height=400, bg="silver")
c.pack()

def kresli_terc(sx,sy,r1,r2,r3):
    c.create_oval(sx-r3, sy-r3, sx+r3, sy+r3, fill="black", width=0)
    c.create_oval(sx-r2, sy-r2, sx+r2, sy+r2, fill="white", width=0)
    c.create_oval(sx-r1, sy-r1, sx+r1, sy+r1, fill="black", width=0)

    c.create_line(0,sy,320,sy,fill="gray")
    c.create_line(sx,sy-170,sx,sy+160,fill="gray")

    c.create_text(sx+10,sy-r1/2,text="50", fill="orange", font="Sans 8")
    c.create_text(sx+10,sy-r3/2,text="40", fill="orange", font="Sans 8")
    c.create_text(sx+10,sy-r2-r1/2,text="10", fill="orange", font="Sans 8")

    c.create_text(sx,sy+r3+40, text="Score:", fill="red", font="Sans 15 bold")
def zasah(sur):
    global skore
    c.create_oval(sur.x-5,sur.y-5,sur.x+5,sur.y+5, fill="red", width=0)
    x1,y1= 160,180
    x2,y2= sur.x,sur.y
    vzd = sqrt((x1-x2)**2+(y1-y2)**2)
    if vzd <= 50:
        skore += 50
    elif vzd <= 100:
        skore += 40
    elif vzd <= 150:
        skore += 10
        
    prepis_skore(skore)
    
def prepis_skore(sskore):
    c.delete("s")
    c.create_text(stredx+50,stredy+190, text=skore, anchor="w", fill="red", font="Sans 15 bold", tags="s")
    
def nova_hra(aaa):
    global skore
    c.delete("all")
    kresli_terc(stredx,stredy,50,100,150)
    skore=0
    
skore=0
stredx,stredy= 160,180
kresli_terc(stredx,stredy,50,100,150)

c.bind("<Button-1>", zasah)
c.bind_all("<Delete>", nova_hra)
