def p(n):
    return n/(7*(10**9))
def e(n):
    return n*365
def o(n):
    return n*(10**3)
x=float(input("How many people do you meet daily: "))
y=float(input("How many people would you consider to be with: "))
z=float(input("How much do you talk to possible targets(out of 10): "))
H=o(z)*p(y)*e(x)
print("Your daily chances: "+str(H))
H=(lambda x: x*20)(H)
print("Your yearly chances: "+str(H))
