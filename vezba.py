brojOsoba=int(input("Unesite broj osoba: "))
listaOsoba=[]
Osoba=[]
for i in range(brojOsoba):
        ime=input("Unesite ime "+str(i+1)+". osobe: ")
        prezime=input("Unesite prezime "+str(i+1)+". osobe: ",)
        brojGodina=int(input("Unesite broj godina "+str(i+1)+ ". osobe: "))
        Osoba.append(ime)
        Osoba.append(prezime)
        Osoba.append(brojGodina)
        listaOsoba.append(Osoba)
        Osoba.remove(ime)
        Osoba.remove(prezime)
        Osoba.remove(brojGodina)
for y in listaOsoba:
    if y[2]<18:
        print("Maloletna osoba:")
        for x in y:
            print(x)
    elif y[2]>=18 and y[2]<65:
        print("Punoletna osoba:")
        for x in y:
            print(x)
    else:
        print("Penzioner: ")
        for x in y:
            print(x)
