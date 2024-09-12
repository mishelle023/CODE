z = 0
while z < 2 or z > 16:
 z = int(input("Zadaj základ sústavy 2 - 16: "))
s = input("Zadaj číslo v {} sústave: ".format(z))
dobre = True # ak je v zadanom reťazci chyba = false
y = 0 # výsledok - číslo v desiatkovej sústave
for c in s:
 #určenie desiatkovej hodnoty hexadecimalneho symbolu
 if c >= '0' and c <= '9':
 x = int(c)
 elif c >= 'a' and c <= 'f':
 x = ord(c) - ord('a') + 10
 elif c >= 'A' and c <= 'F':
 x = ord(c) - ord('A') + 10
 else:
 dobre = False # našiel sa nepovolený znak
 if x >= z:
 dobre = False; # našla sa číslica, ktorá do zadanej sústavy nepatrí
 if dobre:
 y = y * z + x
 else:
 break

if dobre:
    print("Číslo v desiatkovej sústave je ", y)
else:
    print("Zadané číslo obsahuje nepovolený znak, ktorý sa v {}ovej sústave
nepoužíva".format(z))


