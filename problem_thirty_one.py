# multiplier value1 to value2
value1 = int(input("Enter the lower number:"))
value2 = int(input("Enter the upper number:"))
def Multiplier(input1,input2):
    if input1 < input2:
        count = 0
        count1 = 1
        while count <= input2:
            value = input1 * count1
            if value <= input2:
                print(value)
            count = value
            count1+=1
    else:
        print("invalid")        

Multiplier(value1,value2)