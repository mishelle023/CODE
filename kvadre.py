import math
a=float(input())
b=float(input())
c=float(input())

D=(b**2 - 4*a*c)
if D<0:
    print("príklad nemá korene")
elif D>0:
    D= math.sqrt(D)
    x1= (-b+D)/(2*a)
    x2= (-b-D)/(2*a)
    print("Koreň x1: ", x1)
    print("Koreň x2: ", x2)
else:
    x= -b/(2*a)
    print("Rovnica má dvojnásobný koreň")
