# how many inp caraacter have in  there sentence
value= input("Enter a sentence:")
inp = input("Enter the cereter:")
def Myfunction(data,inp):
    val = data.replace(" ", "")
    lst = list(val)
    count = 0
    for i in lst:
        if i == inp:
            count+=1
    if count == 0:
        print(inp,"is not present")
    else:
        print("Occurrence of",inp,"in",data,"=",count)      

Myfunction(value,inp)        


