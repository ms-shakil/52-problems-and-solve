# L C M
import math
a  = int(input("Enter the numer:"))
b  = int(input("Enter the number:"))
def LCM(a,b):   
    if a > b:
        t = a
        a = b
        b = t
    lst = []    
    for i in range(a,1,-1):
        Z = b % i
        X = a % i
        if Z == 0 and X == 0:
            lst.append(i)
            k = b / i
            y = a / i
            b = k
            a = y
    lst.append(a)
    lst.append(b) 
    val = 1       
    for i in lst:
       val*=i 
    print("LCM = ",math.floor(val)) 
LCM(a,b)    

            





