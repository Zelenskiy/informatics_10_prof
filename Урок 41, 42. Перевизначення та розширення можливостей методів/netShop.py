#from shopclases import DeskTable
import shopclases


list = []
# Ручне уведення даних
n = int(input("Скільки товарів бажаєте додати? "))
for t in range(n):
    print("Товар №", t+1, " ", sep="")
    try:
        list.append(shopclases.DeskTable(num="A321" + str(t), title=input("Назва товару "),
                          price=float(input("Вартість в грн "))))   
    except ValueError:
        print ("При уведенні вартості уводимо лише число")
        
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




        
    
