class Machinery:
    def __init__(self, name, price, brand):
        self.brand = brand
        self.name = name
        self.price = price
    def about(self):
        print("Це", self.name)
        print("Вартість", self.price,"грн")

    def __str__(self):
        return self.name

m = Machinery("Мікрохвильова піч", 2000, "LG")
print(m)