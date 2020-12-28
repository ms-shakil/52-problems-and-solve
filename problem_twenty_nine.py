# perfect number !
value = int(input("Enter the number:"))
def Perfect_Number(value):
    count = 0
    for i in range(1,value,1):
        if value % i == 0:
            count+= i
    if count == value:
        print(value,"is perfect number !")
    else:
        print(value,"is not perfect number !")    
Perfect_Number(value)            