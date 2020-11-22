class Stilec:
    color = ''
    mass = 0
    height = 0
    def prezentation(self):
        print("Я стілець. Мій колір", self.color, ".")
        print("Моя маса", self.mass, "кг")

s = Stilec()
s.color = "червоний"
s.mass = 1.2
s.height = 0.6

s.prezentation()
