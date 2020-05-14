#funkcija
def zbir_cifara(broj):
    pom = str(broj)
    povratna = 0
    for i in pom:
        povratna += int(i)
    return povratna

#primer koriscenja
print(zbir_cifara(12487))