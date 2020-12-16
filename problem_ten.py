# this code work  for get factorial number
number = int(input("Enter the number:"))
def Factorial(number):
    num = 1
    for i in range(number):
        var = i* num
        num+= var
    return num   
print("This is factorial number:",Factorial(number))


