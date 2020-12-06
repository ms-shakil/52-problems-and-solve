# addition first first number and last number

import math
number = int(input("Enter the number:"))
msd = number % 10
while number >= 10 :
    number1 = number /10
    number = number1
lsd = math.floor(number)    
value = msd + lsd
print(value)    
