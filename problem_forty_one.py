inp = int(input("Enter the number:"))
def MyFunction(inp):
    for i in range(inp,0,-1):
        if i >=  2:
           print("{}{}{} ".format(2,"^",i,),end= "+")
        elif i <=2:
           print(" 2 + {}".format(i),end ="")   

MyFunction(inp)