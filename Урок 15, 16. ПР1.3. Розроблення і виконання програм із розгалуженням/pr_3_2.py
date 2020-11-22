import math
x = int(input("x = "))
if x < -10:
    f = 3 * x**3 - x**2
elif x >= - 10 and x <= 10:
    f = math.sqrt(10 - x)
else:
    f = 2 * x + 1
print(f)

