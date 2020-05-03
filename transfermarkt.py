lista=[]
petlja=True
while petlja:
    x=int(input("Izaberite opciju (1-Dodaj fudbalera, 2-Izbrisi fudbalera, 3-Kraj): "))
    if x==1:
        ime=input("Unesite ime fudbalera: ")
        prezime=input("Unesite prezime fudbalera: ")
        cena=int(input("Unesite cenu fudbalera: "))
        fudbaler=[ime,prezime,cena]
        lista.append(fudbaler)
    elif x==2:
        imebrisanje=input("Unesite ime fudbalera: ")
        for fudb in lista:
            if fudb[0]==imebrisanje:
                lista.remove(fudb)
    elif x==3:
        petlja=False
    else:
        print("Nepostojeca opcija!\n")
for neko in lista:
    for o in neko:
        print(str(o)+" ")
    print('\n')