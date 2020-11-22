'''
Дано числа 16 і 7. Розробіть програму визна-
чення їх суми, добутку, різниці та ділення пер-
шого на друге з використанням перевизначен-
ня методу. У програмі передбачте створення
суперкласу і двох його підкласів, а також чо-
тирьох методів у різних класах.
'''
class klas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class klas_1(klas):
    def add(self):
        print("Для класу klas_1")
        return self.a + self.b
    def sub(self):
        print("Для класу klas_1")
        return self.a - self.b
    def mul(self):
        print("Для класу klas_1")
        return self.a * self.b
    def div(self):
        print("Для класу klas_1")
        return self.a / self.b

class klas_2(klas):
    def add(self):
        print("Для класу klas_2")
        return self.a + self.b
    def sub(self):
        print("Для класу klas_2")
        return self.a - self.b
    def mul(self):
        print("Для класу klas_2")
        return self.a * self.b
    def div(self):
        print("Для класу klas_2")
        return self.a / self.b

x = klas_1(16,7)
y = klas_2(16,7)

print(x.add())
print(y.mul())


