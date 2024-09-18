from math import sqrt

ax, ay=int(input('ax =')), int(input('ay ='))
bx, by=int(input('bx =')), int(input('by ='))
cx, cy=int(input('cx =')), int(input('cy ='))
c= sqrt(abs(ax-bx)**2 + abs(ay-by)**2)
c= round(c, 2)
a= sqrt(abs(cx-bx)**2 + abs(cy-by)**2)
a= round(a, 2)
b= sqrt(abs(ax-cx)**2 + abs(ay-cy)**2)
b= round(b, 2)
obvod=a+b+c
print(f'Vydialenost bodov A{[ax],[ay]}, B{[bx],[by]},C{[cx],[cy]} je {obvod}')