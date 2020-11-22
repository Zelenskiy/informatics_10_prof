class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        
class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p
        
class DeskTable(Table):
    def area(self):
        return self.width * self.length

a = DeskTable(120, 65, 58)
print(a.length)
print(a.area())

n = KitchenTable(120, 65, 58, 4)
#print(n.length)


