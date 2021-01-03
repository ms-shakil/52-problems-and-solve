# The sum of the streams
inp = int(input("Enter a number:"))
inp2 = int(input("Enter power :"))
def MyFunction(inp,inp2):
    count = 0
    for i in range(0,inp2+1,1):
        value = inp**i
        count += value
    return count
print(MyFunction(inp,inp2)   )  