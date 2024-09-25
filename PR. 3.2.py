from math import sqrt
a= int(input("a= "))
b= int(input("b= "))
c= int(input("c= "))
D=(b**2)-(4*a*c)
if D>0:
    D=sqrt(D)
    x1 = (-b+D)/(2*a)
    x2 = (-b-D)/(2*a)
elif D==0:
    x= (-b)/(2*a)
    print(f"rovnica má jeden koreň x={x}")
else:
    print("rovnica nemá riešenie")
if a<0:
    zn1='-'
if b<0:
    zn2=''
else:
    zn2='+'
if c<0:
    zn3=''
else:
    zn3='+'

if a==1 or a==-1:
    a='x'    
print(f'KR {zn1}{a}^2{zn2}{b}x{zn3}{c}=0 má dva korene x1={round(x1, 2)} a x2={round(x2, 2)}')