Osoba={"ime" : None, "prezime" : None, "godine" : None}
Osoba["ime"]=input("Unesite ime osobe: ")
Osoba["prezime"]=input("Unesite prezime osobe: ")
Osoba["godine"]=int(input("Unesite godine osobe: "))
print("Cao {0} {1}! Imas {2} godina!".format(Osoba["ime"],Osoba["prezime"],Osoba["godine"]))
print("Ovo su svi kvadrati brojeva do 10:")
kvadrati=[i**2 for i in range(1,11)]
kubovi=[i**3 for i in range(1,11)]
print(kvadrati)
print("Ovo su svi kubovi brojeva do 10: ")
print(kubovi)
