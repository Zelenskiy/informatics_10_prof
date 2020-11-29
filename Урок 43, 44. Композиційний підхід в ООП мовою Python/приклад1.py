from math import sqrt, pi

class Kl8_07a:
    def __init__(self,a,b):
        self.plArk = a * b        

class Kl8_07:
    def __init__(self, x, y):
        self.plStola = x * y

    def func1(self):
        self.p1 = Kl8_07a(29.7, 21)
        self.p2 = Kl8_07a(21, 14.85)
        

    def func2(self):
        self.func2 = self.plStola - self.p1.plArk - self.p2.plArk
        

    def func3(self):
        print("Загальна площа =", str(self.plStola), "см²")        
        print("Залишок площі =", str(self.func2), "см²")

ob = Kl8_07(120,90)
ob.func1()
ob.func2()
ob.func3()








a = input()
