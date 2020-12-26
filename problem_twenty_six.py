import math
# 1st ways
value = int(input("Enter the number:"))
def MyFunction(number):
    lst =[]
    while number > 9:
        mod = number % 10
        lst.append(math.floor(mod))
        div = number/10
        number = div
    lst.append(math.floor(number))    
    lenht = len(lst)
    count = 0
    for i in lst:
        count+= i**lenht
    return count
if value == MyFunction(value):
    print(value,"is an armstrong number!")
else:
    print(value, "is not an armstrong numbr!")       


# 2 nd ways


value = int(input("Enter the number:"))
def Armstrong_number(value):
    lst =list(str(value))
    count = 0
    for i in lst:
        count += int(i)**len(lst)
    return count   
if value == Armstrong_number(value):
    print(value,"is an armstrong number:")
else:
    print(value,"is not an armstrong number:")


