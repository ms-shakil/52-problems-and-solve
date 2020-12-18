# count vowels
inp = input("Enter a sentence:")
def MyFunction(inp):
    val = list(inp.replace(" ", ""))
    count = 0
    for i in val:
        if i == "a" or i == "e" or i =="i" or i =="o" or i =="u":
            count +=1
    return count
print("Number of vowels  =",MyFunction(inp))




