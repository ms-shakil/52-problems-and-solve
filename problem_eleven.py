# Find the number of zeros at the end of the factorial number
number = int(input("Enter the number:"))
def Factorial(number):
    num = 1
    for i in range(number):
        var = i* num
        num += var
    count = 0
    arr = list(str(num))
    for i in range(len(arr)-1,0,-1):
        if int(arr[i])== 0:
            count+=1
        if int(arr[i])!= 0:
            break
    return count       
print(Factorial(number))    


