class К17_04:
    def func_1 (self, al, a2): 
        volume = 1/3 * (3.14 * al * al * a2) 
        return volume

    def func_2 (self, a3, a4):
        v = a3 * a3 + a4 * a4 
        surface =	3.14*a3*(a3+math.sqrt(v))
        print("площа = ", surface)

import math

ob1 = К17_04()
ob2 = К17_04()

print ("об'єм = ", ob1.func_1(3, 4)) 
ob2.func_2(4, 5)