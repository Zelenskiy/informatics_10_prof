import math
n = float(input("Уведіть число: "))
try:
    r = math.sqrt(n)
except ValueError:
    print("Недопустимий аргумент")
else:
    print(r)



