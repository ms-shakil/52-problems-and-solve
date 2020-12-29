inp = int(input("Enter lower number:"))
inp1 = int(input("Enter upper number:"))
inp2 = int(input("Enter divison number:"))
def MyFunction(lower,upper,divi):
    for i in range(lower,upper,1):
        mod = i % divi
        if mod == 0:
            print(i)

MyFunction(inp,inp1,inp2)    

