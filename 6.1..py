import string
cislo=int(input("čislo v desiatkovej sústave: "))
radix= int(input("radix číselnej sústavy: "))

def prevod(c,r):
    pom= ''
    #pismena='ABCDEFGHIJKLMNOPQRSTVXYZ'
    pismena = string.ascii_uppercase
    while c != 0:
        zv = c % r
        if zv<10:
            pom = str(zv) + pom
        else:
            idx= zv % 10 #posledna cifra v čisle
            znak = pismena[idx]
            pom = znak + pom
        c = c // r
    return pom

print(f'Číslo {cislo} v desitkovej sústave je {prevod(cislo, radix)} v {radix}-sústava')