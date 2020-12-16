# checking squre numbr
import math
Value = int(input("Enter the number:"))
def squrenumber(val):
    sqr =math.sqrt(val)
    sq = math.floor(sqr)
    if sq*sq == val:
        print("yes")
    else:
        print("no")    
squrenumber(Value)        








