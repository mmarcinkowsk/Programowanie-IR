#!/usr/bin/python3

class Opornik():

    def __init__(self, R=0):
        self.__R = R

    def set_opor(self, R):
        self.__R = R

    def get_opor(self):
        return self.__R



# def szeregowo(opornik1, opornik2):
#     R = opornik1.get_opor() + opornik2.get_opor()
#     return Opornik(R)

# def rownolegle(opornik1:Opornik, opornik2:Opornik)->Opornik:
#     inv_R = 1/opornik1.get_opor() + 1/opornik2.get_opor()
#     return Opornik(1/inv_R)

def szeregowo(*args):
    R = 0
    for opornik in args:
        R += opornik.get_opor()

    return Opornik(R)

def rownolegle(*args):
    inv_R = 0
    for opornik in args:
        inv_R += 1/opornik.get_opor()

    return Opornik(1/inv_R)


opornik1 = Opornik(100)
opornik2 = Opornik(200)

opornik3 = szeregowo(opornik1, opornik2)
opornik4 = rownolegle(opornik1, opornik2)
opornik5 = szeregowo(opornik1, opornik1, opornik1, opornik1, opornik1, opornik1, opornik1, opornik1, opornik1, opornik1)

print(opornik1.get_opor())
print(opornik2.get_opor())
print(opornik3.get_opor())
print(opornik4.get_opor())
print(opornik5.get_opor())
