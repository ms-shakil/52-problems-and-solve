# perfect number 2
value = int(input("Enter the number:"))
def MyFunction(value):
    lst =[]
    for i in range(1,value,1):
        count=0
        for j in range(1,i,1):
            if i % j == 0:
                count+=j
        if count == i:
            lst.append(i)
    return lst        

print(MyFunction(value))