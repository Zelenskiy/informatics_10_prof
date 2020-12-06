class Goods:

    def __init__(self, num="", price=0, title=""):  
        self.num = num
        self.price = price
        self.title = title
    photo = []


class Table(Goods):
    height = 0
    width = 0
    length = 0
    def area(self):
        return self.width * self.length

class DeskTable(Table):
    numberOfDrawers = 0
    numberOfPerson = 1
