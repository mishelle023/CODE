z=0
while z<2 or z>16:
    z= int(input("Zadaj číslo medzi 2 - 16: "))

s= input("Zadaj číslo v {} sústave:".format(z))

dobre = True
y=0

for i in s:

    if i>='0' and i<='9':
        x=int(i)
    elif i>='a' and i<='f':
        x=ord(i) - ord('a') +10
    elif i>='A' and i<='F':
        x=ord(i) - ord('A') +10
    else:
        dobre=False

    if x>= z:
        dobre=False

    if dobre:
        y= y * z + x
    else:
        break

if dobre:
    print("Číslo v desiatkovej sústave", y)
else:
    print("Zadané číslo obsahuje nepovolený znak, ktorý sa v {}ovej sústave nepoužíva".format(z))
