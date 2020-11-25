class Goods:
    # num, title, price, photo
    def __init__(self, num="", price=0, title=""):  #
        self.num = num
        self.price = price
        self.title = title
    photo = []
    #title = ""

class Table(Goods):
    height = 0
    width = 0
    length = 0
    def area(self):
        return self.width * self.length

class DeskTable(Table):
    numberOfDrawers = 0
    numberOfPerson = 1


list = []
# Ручне уведення даних
n = int(input("Скільки товарів бажаєте додати? "))
for t in range(n):
    print("Товар №", t+1, " ", sep="")
    list.append(DeskTable(num="A321" + str(t), title=input("Назва товару "),
                          price=float(input("Вартість в грн "))))   
    
# Вивід даних про товари
print("Наявні товари")
for t in list:
    print("---------------------------")
    print("Назва товару", t.title)
    print("Код товару", t.num)
    print("Вартість", t.price)


'''
t = Table(num="A321546", price=890)
t.title = "Стіл кухонний"
t.height = 0.85
t.width = 0.95
t.length = 1.25
s = t.area()

print("Дані про товар")
print(t.title)
#(85x95x125)
print("(", int(t.height*100), "x",int(t.width*100), "x", int(t.length*100), ")", sep="")
'''




        
    
