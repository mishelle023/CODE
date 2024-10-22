x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

def koeficienty(x1,x2,y1,y2):
    aa = -(y2 - y1)
    bb= x2 - x1
    cc= -(aa*x1) - (bb*y1)
    return aa,bb,cc

def znamienka(pom):
    if pom >= 0:
        znamienko = '+'
    else:
        znamienko = ''
    return znamienko
a,b,c = koeficienty(x1,x2,y1,y2)
znamB, znamC = znamienka(b), znamienka(c)
print(f'VRP určenej bodmi [{x1},{y1}] a [{x2},{y2}] je: {a}.x {znamB} {b}.y {znamC} {c} = 0')