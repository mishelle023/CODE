cislo=int(input("Zadaj desiatkové číslo:"))

binarne=""
podiel=cislo

while podiel>0:
    binarne=str(podiel%2)+binarne
    podiel=podiel//2

print(binarne)