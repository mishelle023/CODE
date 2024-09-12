hx = input("Zadaj číslo v šestnástkovej sústave: ")
dobre = True
y = 0
for c in hx:
    if c >= '0' and c <= '9':
        x = int(c)
    elif c >= 'a' and c <= 'f':
        x = ord(c) - ord('a') + 10
    elif c >= 'A' and c <= 'F':
        x = ord(c) - ord('A') + 10
    else:
        dobre = False
    if dobre:
        y = y * 16 + x
    else:
        break

if dobre:
 print("Číslo v desiatkovej sústave je ", y)
else:
 print("Zadané hexadecimálne číslo obsahuje nepovolený znak")
