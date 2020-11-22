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
    def discountPrice(self, discount):
        return self.price * (1-discount / 100)     
    def about(self):
        print("Холодильник марки", self.brand)
        print("Вартість", self.price,"грн")   

# Ручне уведення
n = int(input("Уведіть кількість одиниць обладнання "))
list = []
for i in range(1,n+1):
    print("----------------------------------")
    print("Уведемо дані елемента №",i)
    list.append(Refrigerator(input("Назва обладнання "), 
    int(input("Ціна ")), input("Фірма виробник "), 
    int(input("Потужність ")), int(input("Кількість камер "))))

# Сортуємо по вартості
list.sort(key=lambda x: x.price, reverse=True)

# Виводимо список обладнання
print("----------------------------------")
print("Список обладнання")
print("----------------------------------")
for m in list:
    print("Назва обладнання", m.name)
    print("Ціна обладнання", m.price, "грн")
    print("Потужність", m.power)
    print("Кількість камер", m.numberOfCameras)
    m.about()
    print("----------------------------------")






#m = Refrigerator("Холодильник", 11000, "Samsung")
# m = Refrigerator("Холодильник", 11000, "Samsung", 800, 2)
# m.about()
# print("Вартість зі знижкою", m.discountPrice(20))

