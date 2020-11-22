def avg(x):
    sum_values = sum(x)
    count_values = len(x)
    return sum_values / count_values

x1 = [2, 3, 4]
x2 = (2, 3, 4)

print(avg(x1))
print(avg(x2))

