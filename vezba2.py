x=[]
y=1
while y!=0:
    y=int(input("Unesite neki broj: "))
    if y!=0:
        x.append(y)
print(max(x))
print(min(x))