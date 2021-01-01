# The coordinate point is inside or outside the circle find
import math
x1 = int(input("Enter coordinate x1:"))
y1 = int(input("Enter coordinate y1:"))
x2 =int(input("Enter coordinate x2:"))
y2 = int(input("Enter coordinate y2:"))
z = int(input("Enter the basarddo:"))

def MyFunction(x1,x2,y1,y2,z):
    value = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    if value <= z:
        print("The point is inside the circle.")
    else:
        print("The point is not inside the circle.")
MyFunction(x1,x2,y1,y2,z)    