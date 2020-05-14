#napisana funkcija, 0 ne priznaje kao pozitivan broj, valjda je to okej
def broj_pozitivnih(lista):
    brojac = 0
    for i in lista:
        if i > 0:
            brojac+=1
    return brojac

#primer poziva
print(broj_pozitivnih([2,-1,3,0,-5,1,9]))