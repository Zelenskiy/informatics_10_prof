import math
class Figures:
    name = ''
    flat = True

class Chotirikutnik(Figures):
    angleCount = 4
    ploshcha = 0
    storona1 = 0
    storona2 = 0
    storona3 = 0
    storona4 = 0
    
class Pramokutnik(Chotirikutnik):
    name = 'прямокутник'
    perimetr = 0
    def getSquare(self):
        return self.storona1 * self.storona2
    def getPerimetr(self):
        return 2 * (self.storona1 + self.storona2)

class Trikutnik(Figures):
    storona1 = 0
    storona2 = 0
    storona3 = 0
    angleCount = 3
    def getSquare(self):
        p
        return math.sqrt(

p = Pramokutnik()
p.storona1 = 12
p.storona2 = 10
print("Площа прямокутника", p.getSquare())
print("Периметр прямокутника", p.getPerimetr())
