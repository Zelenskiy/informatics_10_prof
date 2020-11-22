class Document:
    def __init__(self, tip, num, seria='ВП'):
        self.tip = tip
        self.num =num
        self.seria = seria  
    
    name = ''
    sname = ''    
    
    def output(self):
        print("Тип документа", self.tip)
        print("Видано на", self.sname, self.name)

d1 = Document(tip="Водійське посвічення", num=324, seria='ВПП')

d1.sname = "Петренко"
d1.name = "Леонід"

d1.output()
print("Серія та номер документа",d1.seria, "№", d1.num)


