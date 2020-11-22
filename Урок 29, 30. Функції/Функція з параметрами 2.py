def avg(a, b, c):
    sum_values = a + b + c
    count_values = 3
    return sum_values / count_values

x1 = [2, 3, 4]
x2 = (2, 3, 4)

print(avg(*x1))
print(avg(*x2))

