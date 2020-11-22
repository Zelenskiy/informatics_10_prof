class Document:
    tip = ''
    name = ''
    sname = ''
    num = 0
    seria = ''
    def output(self):
        print("Тип документа", self.tip)
        print("Видано на", self.sname, self.name)

d1 = Document()
d1.tip ="Водійське посвічення"
d1.sname = "Петренко"
d1.name = "Леонід"
d1.num =324
d1.seria = 'ВП'

d1.output()
print("Серія та номер документа",d1.seria, "№", d1.num)


