from math import sqrt

ax, ay=int(input('ax =')), int(input('ay ='))
bx, by=int(input('bx =')), int(input('by ='))
vzd= sqrt(abs(ax-bx)**2 + abs(ay-by)**2)
vzd= round(vzd, 2)

print(f'Vydialenost bodov A{[ax],[ay]} a B{[bx],[by]} je {vzd}')