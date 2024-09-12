print("Prosím, zadaj číslo")
cislo1=int(input())
print("Prosím, zadaj ďalšie číslo")
cislo2=int(input())
print("Prosím, zadaj akú operáciu chceš urobiť")
znamienko=input()

if znamienko == "+":
    vysledok = cislo1+cislo2
elif znamienko == "-":
    vysledok = cislo1-cislo2
elif znamienko == "*":
    vysledok = cislo1*cislo2
else:
    vysledok = cislo1/cislo2

print(vysledok)

