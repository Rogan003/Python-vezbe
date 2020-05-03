def ListToString(list):
    string=""
    for i in list:
        string+=i
    return string
eng=""
while eng!="aezakmi":
    eng=input("Enter a word in English: ")
    duzina=len(eng)-1
    pom=duzina
    alien=[i for i in range(duzina+1)]
    while duzina!=-1:
        alien[pom-duzina]=eng[duzina]
        duzina-=1
    print("Alien word: "+str(ListToString(alien)))