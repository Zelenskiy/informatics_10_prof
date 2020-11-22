'''
21 14
7
НСД (найб. сп. дільник) Евкліда

21 14
7  14
7  7
7 НСД

13 11
2  11
2  9
2  7
2  5
2  3
2  1
1  1
1 НСД
'''
a = int(input("a = "))
b = int(input("b = "))

while (a != b):
    if a > b:
        a = a - b    # a -= b
    else:
        b = b - a    # b -= a

print("GCD  =", a)
