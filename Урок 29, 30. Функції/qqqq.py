
def add(a, b, c):
    s = a + b + c # s - локальна
    return s


#a1 = 5   # глобальні змінні
#b1 = 2
#c1 = 0

#d = add(a1, b1, c1)

#print(d)


def func1(a, b):
    s = a + b
    r = a - b
    return s, r

a = 5
b = 9

d, t = func1(a, b)
print (a, b)




    

