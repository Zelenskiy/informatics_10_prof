class Obj_1:
    def __init__(self,a):
        self.a = a
    def __add__(self, b):
        self.a += b

obj1 = Obj_1(23)
obj2 = Obj_1(5)
obj1 + obj2
print(obj1.a)
