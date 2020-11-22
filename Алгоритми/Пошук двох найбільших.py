m = [328, 228, 12, 11, 14, 2, 228, 6, 0, 9, 7, 2, 5]

m1 = m[0]
m2 = m[1]
if m1 > m2:
    m2, m1 = m1, m2

for x in m:
    if x > m1:
        m2 = m1
        m1 = x
    else:
        if x > m2:
            m2 =x
        
print (m1, m2)
