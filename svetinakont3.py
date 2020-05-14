#funckija zbir_cifara
def zbir_cifara(broj):
    pom = str(broj)
    povratna = 0
    for i in pom:
        povratna += int(i)
    return povratna

#tvoj sudbinski, nema ifova jer je jednocifren
print(zbir_cifara(10122003))

#funkcija za sudbinski
def sudbinski_broj(broj):
    sudbinski = zbir_cifara(broj)
    while sudbinski > 9:
        sudbinski = zbir_cifara(sudbinski)
    return sudbinski

#primer koriscenja funkcije
print(sudbinski_broj(15052001))