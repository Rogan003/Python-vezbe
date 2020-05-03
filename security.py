def pronalazak(nesto):
    string=""
    mesto=0
    for i in nesto:
        if i=='G':
            if mesto==1:
                string+="quiet"
            else:
                string+="ALARM"
        elif i=='T':
            mesto+=1
        elif i=='$':
            mesto+=1
    return string
unos=input("Unesite mapu: ")
print(pronalazak(unos))