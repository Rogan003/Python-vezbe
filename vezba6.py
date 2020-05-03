class Trougao:
    def __init__(self,a,b,c):
        assert a>0 and b>0 and c>0, "Stranica manja ili jednaka 0!"
        self.__a=a
        self.__b=b
        self.__c=c
    def __add__(self,other):
        self.__a+=other.__a
        self.__b+=other.__b
        self.__c+=other.__c
    def __sub__(self,other):
        assert self.__a>other.__a and self.__b>other.__b and self.__c>other.__c, "Drugi trougao veci ili jednak od prvom"
        self.__a-=other.a
        self.__b-=other.b
        self.__c-=other.c
    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property
    def c(self):
        return self.__c
    @a.setter
    def a(self,vrednost):
        assert vrednost>0, "Stranica manja ili jednaka 0!"
        self.__a=vrednost
    @b.setter
    def b(self,vrednost):
        assert vrednost>0, "Stranica manja ili jednaka 0!"
        self.__b=vrednost
    @c.setter
    def c(self,vrednost):
        assert vrednost>0, "Stranica manja ili jednaka 0!"
        self.__c=vrednost
class JKKTrougao(Trougao):
    def __init__(self,a,b):
        assert a>0 and b>0, "Stranica manja ili jednaka 0!"
        self.__a=a
        self.__b=b
        self.__c=b
    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property
    def c(self):
        return self.__c
    @a.setter
    def a(self,vrednost):
        assert vrednost>0, "Stranica manja ili jednaka 0!"
        self.__a=vrednost
    @b.setter
    def b(self,vrednost):
        assert vrednost>0, "Stranica manja ili jednaka 0!"
        self.__b=vrednost
        self.__c=vrednost
    @c.setter
    def c(self,vrednost):
        assert vrednost>0, "Stranica manja ili jednaka 0!"
        self.__c=vrednost
        self.__b=vrednost
def jks(trougao):
    if(trougao.a==trougao.b and trougao.b==trougao.c):
        return True
    else:
        return False
kvadrat=lambda x: x**2
t=Trougao(3,4,5)
jkkt=JKKTrougao(7,8)
jkks=JKKTrougao(6,6)
print(str(t.a)+" "+str(t.b)+" "+str(t.c))
print(str(jkkt.a)+" "+str(jkkt.b)+" "+str(jkkt.c))
print(str(jkks.a)+" "+str(jkks.b)+" "+str(jkks.c))
if(jks(jkks)):
    print("Kvadrat stranica jks trogla: "+str(kvadrat(jkks.a)))
t.a=5
t.b=7
t.c=9
print(str(t.a)+" "+str(t.b)+" "+str(t.c))