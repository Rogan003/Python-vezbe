import re
def check(pas):
    string=""
    znaci=r"([\!\@\#\$\%\&\*])"
    brojevi=r"([0-9])"
    if(len(pas)>=7 and len(re.findall(znaci,pas))>=2 and len(re.findall(brojevi,pas))>=2):
        string+="Strong"
    else:
        string+="Weak"
    return string
while True:
    password=input("Enter your password: ")
    print(check(password))
