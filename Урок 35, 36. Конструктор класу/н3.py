class Country:
    def __init__(self, a):
        self.a = a;

obj1 = Country("Україна")
obj2 = Country("Франція")

n = int(input("Уведіть ціле число"))
if n > 5:
    print(obj1.a)
else:
    print(obj2.a)
