'''

'''
a = int(input("a = "))
b = int(input("b = "))

d = a * b

while (b !=0):
    a = a % b    #Залишок від ділення a на b a %= b
    a, b = b, a  #Обмінюємо значення змінних a та b
    

print("НСК  =", int(d / a))
