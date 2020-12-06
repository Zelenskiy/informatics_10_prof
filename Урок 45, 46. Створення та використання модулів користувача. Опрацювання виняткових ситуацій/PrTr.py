try:
    a = float(input("Введіть перший катет "))
    b = float(input("Введіть другий катет "))
except ValueError:
    print("Уведено не числа")
else:    
    import math
    c = math.sqrt(a**2 + b**2)
    print("Гіпотенуза дорівнює ", c)


    
    
