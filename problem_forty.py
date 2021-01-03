# The sum of the streams 2
inp = int(input("Enter the number:"))
def Myfunction(inp):
    count= 0
    for i in range(inp):
        add =1
        for  j in range(i):
            kk = j*add
            add += kk 
        nn =i/add
        count+=nn
    return count        
print(Myfunction(inp))    