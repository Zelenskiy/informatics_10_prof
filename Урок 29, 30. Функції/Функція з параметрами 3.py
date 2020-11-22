def avg(a, b, c):
    sum_values = a + b + c
    count_values = 3
    return sum_values / count_values

x1 = [2, 3, 4]
x3 = {'a': 2, 'b': 3, 'c': 4}

print(avg(*x1))

print(avg(**x3))

