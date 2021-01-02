# reverse a number
inp = int(input("Enter the number:"))
def MyFunction(inp):
    value = list(str(inp))
    value.reverse()
    val ="".join(value)
    return int(val)
print(MyFunction(inp))