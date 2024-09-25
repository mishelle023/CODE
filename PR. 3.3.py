a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a < b:
    if a<c:
        print(f'najmensie cislo je a= {a}')
    else:
        print(f'najmnsie cislo je c= {c}')
elif b<c:
    print(f'najmensie cislo je b= {b}')
else:
    print(f'najmensie cislo je c= {c}')