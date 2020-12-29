inp = int(input("Enter divi 1: "))
inp2 = int(input("Enter divi 2 :"))
inp3 = int(input("Enter value:"))
def MyFunction(div1,div2,value):
    for i in range(1,value,1):
        mod = i % div1
        mod1 = i % div2
        if mod ==0 and mod1==0:
            print(i)
MyFunction(inp,inp2,inp3)








