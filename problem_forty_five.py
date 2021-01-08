#area of triangle
import math
a=int(input("Enter value1:"))
b=int(input("Enter value2:"))
c=int(input("Enter value3:"))
def MyFunction(a,b,c):
    s= (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return round(area,3)

print("Area =",MyFunction(a,b,c))

