a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
x = int(input("xM = "))
y = int(input("yM = "))
if (b<0):
    op2 = ''
else:
    op2 = '+'
    
if (c<0):
    op3 = ''
else:
    op3 = '+'
if a*x+b*y+c == 0:
    pom= ''
else:
    pom= 'ne'
print(f'Bod M{[x], [y]} {pom}leží {a}x{op2}{b}y{op3}{c}=0')