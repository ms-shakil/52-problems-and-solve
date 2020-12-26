value = int(input("Enter food range:"))
def MyFunction(value):
    count =0
    while value > 1:
        count+=1
        val = value / 2
        value = val
    return count

print(MyFunction(value),"dayes")