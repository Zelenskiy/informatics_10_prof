def add(*x):
    line = ""
    sum_values = 0            
    for element in x:
        if type(element) == str:
            line += element
        else:
            sum_values += element
    
    if type(element) == str:
        return line
    else:
        return sum_values     

#print (add(3, 5, 6))
#print (add('3', '5', '6'))
print (add(3, "4", "G", 2))
#print (add('3'))
