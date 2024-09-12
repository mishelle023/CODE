import tkinter, random
print("Napíš svoje meno")
meno=input()
print("V ako meste bývaš?")
mesto=input()
print("Zdravím ťa,", meno, "z", mesto, "!")
print("Koľko vážiš?")
vaha=int(input())
if 100>vaha:
    print(meno, ", si veľmi ťažky")
else:
    print(meno, ", tvoja váha je v pohode")
print("Čísla deliteľné číslom 7 a zároveň menšie ako tvoja váha sú:")
for i in range(vaha+1):
    if (i%7==0)and (i<vaha):
        print(i, end=","+"\n")
print("Obsah štvorca so stranou takou dlhou, ako je tvoja váha je:")
print(vaha*vaha)

p=tkinter.Canvas(width=300, height=500, bg="white")
p.pack()


a=random.randrange(1,90)

for i in range(40):
    x=random.randrange(300)
    y=random.randrange(500)
    if a<50:
        p.create_oval(x,x+a,y,y+a, fill="red")
    else:
        p.create_oval(x,x+a,y,y+a, fill="blue")
