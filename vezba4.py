stranice=[]
for i in range(3):
    stranice.append(int(input("Unesite velicinu stranice: ")))
    print(stranice[i])
    assert (stranice[i]>0), "Stranice manja od 0!"
fajl=open("fajl.txt","w")
try:
    while True:
        a=int(input("Unesite neki broj: "))
        fajl.write(str(sum(stranice)/a)+"\n")
except ZeroDivisionError:
    print("Nemoguce je podeliti broj sa 0!")
finally:
    fajl.close()
    fajl=open("fajl.txt","r")
    for x in fajl:
        print(x)
    fajl.close()