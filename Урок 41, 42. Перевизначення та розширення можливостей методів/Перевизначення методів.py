class Machinery:
    def __init__(self, name, price, brand):
        self.brand = brand
        self.name = name
        self.price = price
    def about(self):
        print("Це", self.name)
        print("Вартість", self.price,"грн")

class Refrigerator(Machinery):
    def __init__(self, name, price, brand, power, numberOfCameras):
        Machinery.__init__(self, name, price, brand)
        self.power = power
        self.numberOfCameras = numberOfCameras
    def wholesalePrice(self, discount):
        return self.price * (1-discount / 100)        


m = Refrigerator("Холодильник", 11000, "Samsung", 800, 2)
m.about()
print("Вартість зі знижкою", m.wholesalePrice(20))

